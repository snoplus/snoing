#!/usr/bin/env python
#
# System
#
# Initailises the install folder, checks the system and executes commands. All exceptions that 
# snoing can/should be raised should come from this file.
#
# Author P G Jones - 21/09/2012 <p.g.jones@qmul.ac.uk> : First revision
####################################################################################################
import os
import snoing_exceptions
import subprocess
import urllib2
import tarfile
import shutil
import pickle
import base64
import sys
import snoing_tarfile
import installmode

class System(object):
    """ System object, holds information about the install folder and allows commands to be 
    executed.
    """
    Mac, Linux = range(2)
    def __init__(self, logger, cache_path, install_path, install_mode=None, arguments=[]):
        """ Initialise with a logger for output and a prefered cache and install path. The 
        install_mode is optional, None is no install mode required. The arguments are extra 
        arguments applied to all configure script calls (package specific).
        """
        self._logger = logger
        self._check_clean_environment()
        self._cache_path = self.build_path(cache_path)
        self._install_path = self.build_path(install_path)
        self._arguments = arguments
        # Check the system type, only concerned about mac or linux
        if os.uname()[0] == "Darwin":
            self._os_type = System.Mac
            # Setup the mac environment, first find fink or ports and set a special mac environment
            fink_path = self.find_library("fink")
            ports_path = self.find_library("port")
            mac_dir = None
            if fink_path is not None and ports_path is not None: # Both fink and ports exist
                self._logger.warn("Both Fink and Ports exist, will use fink.")
                mac_dir = fink_path.strip().replace("/bin/fink","")
            elif fink_path is not None:
                mac_dir = fink_path.strip().replace("/bin/fink","")
            elif ports_path is not None:
                mac_dir = fink_path.strip().replace("/bin/port","")
            if mac_dir is not None: # A special mac path exists, add to environment
                self._append_environment("PATH", os.path.join(mac_dir,"bin"))
                self._append_environment("LIBRARY_PATH", os.path.join(mac_dir,"lib"))
                self._append_environment("CPLUS_INCLUDE_PATH", os.path.join(mac_dir,"include"))
            # Check if XCode in 10.7 installs X11 to /usr/X11
            if os.path.exists("/usr/X11"):
                self._append_environment("PATH", "/usr/X11/bin")
                self._append_environment("LIBRARY_PATH", "/usr/X11/lib")
                self._append_environment("CPLUS_INCLUDE_PATH", "/usr/X11/include")
            # Check if frameworks is used
            if os.path.exists("/System/Library/Frameworks"):
                self._append_environment("CPLUS_INCLUDE_PATH", "/System/Library/Frameworks")
        else: # So much easier for Linux systems....
            self._os_type = System.Linux
        # Check the install mode status of the install_path
        settings_path = os.path.join(self._install_path, "snoing.pkl")
        self._install_mode = self._deserialise(settings_path)
        if isinstance(self._install_mode, dict):
            if self._install_mode['Graphical'] == 1:
                self._install_mode = installmode.Graphical
            elif self._install_mode['Grid'] == 1:
                self._install_mode = installmode.Grid
        if self._install_mode is not None: # Settings exist for install path
            if self._install_mode is not install_mode: # Existing settings do not match
                raise snoing_exceptions.InstallModeException("Install mode mismatch.", 
                                                             self._install_mode, install_mode)
        else:
            self._serialise(settings_path, install_mode)
        self._install_mode = install_mode
        # All good if we get here
        self._logger.set_install_path(os.path.join(self.get_install_path(), "snoing.log"))
        self._logger.info("System ready.")
        self._logger.info("Caching to " + self._cache_path)
        self._logger.info("Installing to " + self._install_path)
        self._logger.info("System is " + ' '.join(os.uname()))
####################################################################################################
    # Functions that are publically useful and available
    def get_cache_path(self):
        """ Return the cache path."""
        return self._cache_path
    def get_install_path(self):
        """ Return the install path."""
        return self._install_path
    def get_install_mode(self):
        """ Return the system install mode."""
        return self._install_mode
    def get_os_type(self):
        """ Return the system os type."""
        return self._os_type
####################################################################################################
    # Functions that do stuff to the system
    def configure_command(self, command='./configure', args=[], cwd=None, env={}, verbose=False):
        """ Execute a configure command, add the extra arguments."""
        if cwd is None:
            cwd = self.get_install_path()
        args.extend(self._arguments)
        self.execute_command(command, args, cwd, env, verbose)
    def execute_command(self, command, args=[], cwd=None, env={}, verbose=False):
        """ Execute the command with args, extra environment env in the path cwd."""
        if cwd is None:
            cwd = self.get_install_path()
        # Firstly setup the environment
        local_env = os.environ.copy()
        for key in env.iterkeys():
            self._append_environment(key, env[key], local_env)
        # Now open and run the shell_command
        shell_command = [command] + args
        process = subprocess.Popen(args=shell_command, env=local_env, cwd=cwd, 
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = ""
        error = ""
        self._logger.command(command + ' ' + ' '.join(args))
        if verbose or self._logger.is_verbose():
            for line in iter(process.stdout.readline, ""):
                sys.stdout.write('\n' + line[:-1])
                sys.stdout.flush()
                self._logger.detail(line[:-1])
                output += '\n' + line[:-1]
            process.wait()
        else:
            output, error = process.communicate()
        if output != "":
            self._logger.detail(output)
        if error != "":
            self._logger.detail(error)
        # After process has finished
        if process.returncode != 0:
            raise snoing_exceptions.SystemException("Command returned %i" % process.returncode,
                                                    output)
        return output # Very useful for library checking
    def execute_complex_command(self, command, verbose=False):
        """ Execute a multiple line bash command, writes to a temp bash file then executes it. The 
        environment is assumed to be set in the commands.
        """
        file_name = os.path.join(self.get_install_path(), "temp.sh")
        command_file = open(file_name, "w")
        command_file.write(command)
        command_file.close()
        self._logger.command(command + ">>" + file_name)
        output = self.execute_command("/bin/bash", args=[file_name], verbose=verbose)
        os.remove( file_name )
    def download_file(self, url, username=None, password=None, token=None, file_name=None):
        """ Download the file at url, using either username+password or token authentication if 
        supplied and needed. The optional file_name parameter will save the url to a file named 
        file_name.
        """
        # Firstly build the request header
        url_request = urllib2.Request(url)
        if username is not None: # HTTP authentication supplied
            b64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
            url_request.add_header("Authorization", "Basic %s" % b64string)
        elif token is not None:
            url_request.add_header("Authorization", "token %s" % token)
        if file_name is None:
            file_name = url.split('/')[-1]
        file_path = os.path.join(self.get_cache_path(), file_name)
        local_file = open(file_path, 'wb')
        try:
            self._logger.command("wget " + url)
            remote_file = urllib2.urlopen(url_request)
            download_size = int(remote_file.info().getheaders("Content-Length")[0])
            local_file.write(remote_file.read())
            local_file.close()
            remote_file.close()
        except urllib2.URLError, e: # Server not available
            os.remove(file_path)
            raise snoing_exceptions.SystemException("Download error", url)
        self._logger.detail("Downloaded %i bytes\n" % download_size)
    def untar_file(self, file_name, target_path, strip=0):
        """ Untar file_name to target_path striping the first strip folders."""
        self._logger.command("untar " + file_name)
        if os.path.exists(target_path):
            shutil.rmtree(target_path)
        if strip == 0: # Untar directly into target
            tar_file = tarfile.open(os.path.join(self.get_cache_path(), file_name))
            tar_file.__class__ = snoing_tarfile.TarFile
            tar_file.extractall(target_path)
            tar_file.close()
        else: # Must extract to temp target then copy strip directory to real target 
            temp_dir = os.path.join(self.get_cache_path(), "temp")
            if os.path.exists(temp_dir): # Delete temp if it exits
                shutil.rmtree(temp_dir)
            temp_dir = self.build_path(temp_dir)
            tar_file = tarfile.open(os.path.join(self.get_cache_path(), file_name))
            tar_file.__class__ = snoing_tarfile.TarFile
            tar_file.extractall(temp_dir)
            tar_file.close()
            copy_dir = temp_dir
            for iStrip in range(0, strip):
                sub_folders = os.listdir(copy_dir)
                if 'pax_global_header' in sub_folders:
                    sub_folders.remove('pax_global_header')
                copy_dir = os.path.join(copy_dir, sub_folders[0])
            shutil.copytree(copy_dir, target_path)
            shutil.rmtree(temp_dir)
    def remove(self, path):
        """ Remove a directory."""
        shutil.rmtree(path)
####################################################################################################
    # Functions that search the system for things
    def find_library(self, library):
        """ Search the system for a library, return its location if found otherwise return None."""
        output = self.execute_command("whereis", [library])
        output = output.split('\n')[1]
        location = output.split(':')
        if len(location)==1:
            if location[0] == "\n" or location[0] == "":
                return None
            else:
                return location[0]
        else:
            if location[1] == "\n" or location[1] == "":
                return None
            else:
                return location[1]
    def library_exists(self, library, path):
        """ Check that the library exists in the path, will check correct extensions."""
        return os.path.exists(os.path.join(path, library + ".a")) or \
            os.path.exists(os.path.join(path, library + ".so")) or \
            os.path.exists(os.path.join(path, library + ".dylib"))
    def file_exists(self, file_name, path=None):
        """ Check that a file exists."""
        if path is None:
            path = self.get_cache_path()
        return os.path.exists(os.path.join(path, file_name))
    def test_library(self, library, headers=[]):
        """ Test if code can be compiled with header and linked to libName."""
        if self._os_type == System.Mac:
            return self._test_compile(headers, ["-l%s" % library]) or \
                self._test_compile(headers, ["-framework","%s" % library])
        else:
            return self._test_compile(headers, ["-l%s" % library])
    def test_config(self, config, headers=[]):
        """ Test if code can be compiled using a xxx-config command."""
        output = self.execute_command(config, ['--libs'])
        libs = output.strip('\n').split(' ')
        output = self.execute_command(config, ['--includes'])
        includes = output.strip('\n').split(' ')
        return self._test_compile(headers, libs + includes)
    def build_path(self, path):
        """ Change the path into a global path and ensure the path exists."""
        globalPath = path
        if path[0] != '/': # Global path
            globalPath = os.path.abspath(os.path.join(os.getcwd(), path ))
        if not os.path.exists(globalPath):
            os.makedirs(globalPath)
        return globalPath
####################################################################################################
    # Useful internal functions
    def _test_compile(self, headers=[], flags=[]):
        """ Test code compiles with the headers and flags. Returns True or False tuple with output"""
        file_text = ""
        for header in headers:
            file_text += "#include <%s>\n" % header
        file_text += "int main( int a, char* b[] ) { }"
        file_name = os.path.join(self.get_cache_path(), "temp.cc")
        test_file = open(file_name, "w")
        test_file.write(file_text)
        test_file.close()
        try:
            output = self.execute_command("g++", [file_name] + flags)
            os.remove( file_name )
            self._logger.detail(output)
            return True
        except snoing_exceptions.SystemException, e:
            os.remove( file_name )
            return False

    def _check_clean_environment(self):
        """ Check the environment is clean (mainly no G4 variables)."""
        for env in os.environ.itervalues():
            inenv = env.find('G4')
            if inenv!=-1:
                self._logger.error("System not clean")
                raise snoing_exceptions.SystemException("System not clean", env)
    def _serialise(self, path, data):
        """ Pickle data to path."""
        data_file = open(path, "w")
        pickle.dump(data, data_file)
        data_file.close()
    def _deserialise(self, path):
        """ Unpickle data from path."""
        if os.path.isfile(path):
            data_file = open(path, "r")
            data = pickle.load(data_file)
            data_file.close()
            return data
        else:
            return None
    def _append_environment(self, key, value, env=os.environ):
        """ Append the value to environment (env) variable key, if key exists, if not make it."""
        if key in env:
            env[key] = "%s:%s" % (value, env[key])
        else:
            env[key] = value
