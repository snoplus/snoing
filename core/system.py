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
import subprocess
import urllib2
import tarfile
import shutil
import pickle

class System(object):
    """ System object, holds information about the install folder and allows commands to be 
    executed.
    """
    Mac, Linux = range(2)
    def __init__(self, logger, cache_path, install_path, install_mode=None):
        """ Initialise with a logger for output and a prefered cache and install path. The 
        install_mode is optional, None is no install mode required.
        """
        self._logger = logger
        self._check_clean_environment()
        self._cache_path = self._build_path(cache_path)
        self._install_path = self._build_path(install_path)
        # Check the system type, only concerned about mac or linux
        if os.uname()[0] == "Darwin":
            self.os_type = Mac
            # Setup the mac environment, first find fink or ports and set a special mac environment
            fink_path = self._Find("fink")!!
            ports_path = self._Find("port")!!
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
            self.os_type = Linux
        # Check the install mode status of the install_path
        settings_path = os.path.join(self._install_path, "snoing.pkl")
        self._install_mode = self._deserialise(settings_path)
        if self._install_mode is not None: # Settings exist for install path
            if self._install_mode is not install_mode: # Existing settings do not match
                self._logger.error!
                raise !!
            else:
                self._serialise(settings_path)
        # All good if we get here
        self._logger.set_state("System ready.")!
####################################################################################################
    # Functions that are publically useful and available
    def get_cache_path(self):
        """ Return the cache path."""
        return self._cache_path
    def get_install_path(self):
        """ Return the install path."""
        return self._install_path
####################################################################################################
    # Functions that do stuff to the system
    def execute_command(self, command, args=[], cwd=self.get_install_path(), env={}, verbose=False):
        """ Execute the command with args, extra environment env in the path cwd."""
        # Firstly setup the environment
        local_env = os.environ.copy()
        for key in env:
            self._append_environment( key, env[key], local_env )
        # Now open and run the shell_command
        shell_command = [command] + args
        process = subprocess.Popen(args=shellCommand, env=local_env, cwd=cwd, 
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = command + ' '.join( args ) + '\n'
        if verbose:
            for line in iter( process.stdout.readline, "" ):
                sys.stdout.write( '\n' + line[:-1] )
                sys.stdout.flush()
                output += '\n' + line[:-1]
            process.wait()
        else:
            output, error = process.communicate()
        output += "\n%s" % error
        # After process has finished
        if process.returncode != 0:
            raise !!
        return output
    def execute_complex_command(command, verbose=False):
        """ Execute a multiple line bash command, writes to a temp bash file then executes it. The 
        environment is assumed to be set in the commands.
        """
        file_name = os.path.join(self.get_install_path(), "temp.sh")
        command_file = open(file_name, "w")
        command_file.write(command)
        command_file.close()
        output = self.execute_command("/bin/bash", args=[file_name], verbose=verbose)
        os.remove( file_name )
        return output
    def download_file(url, username=None, password=None, token=None, file_name=None):
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
        local_file = open(os.path.join(self.get_cache_path(), file_name), 'wb')
        try:
            remote_file = urllib2.urlopen(url_request)
            download_size = int(remoteFile.info().getheaders("Content-Length")[0])
            local_file.write(remote_file.read())
            local_file.close()
            remote_file.close()
        except urllib2.URLError, e: # Server not available
            os.remove(local_file)
            raise !!
        return "Downloaded %i bytes\n" % download_size
    def untar_file(file_name, target_path, strip=0):
        """ Untar file_name to target_path striping the first strip folders."""
        if strip == 0: # Untar directly into target
            tar_file = tarfile.open(os.path.join(self.get_cache_path(), file_name))
            tar_file.extractall(target_path)
            tar_file.close()
        else: # Must extract to temp target then copy strip directory to real target 
            temp_dir = os.path.join(self.get_cache_path(), "temp")
            if os.path.exists(temp_dir): # Delete temp if it exits
                shutil.remove(temp_dir)
            tar_file = tarfile.open(os.path.join(self.get_cache_path(), file_name))
            tar_file.extractall(temp_dir)
            tar_file.close()
            copy_dir = temp_dir
            for iStrip in range(0, strip):
                sub_folders = os.listdir(copy_dir)
                if 'pax_global_header' in sub_folders:
                    sub_folders.remove('pax_global_header')
                copy_dir = os.path.join(copy_dir, subFolders[0])
            shutil.copytree(copy_dir, target_path)
            shutil.rmtree(temp_dir)
        return "Extracted %s to %s" % (file_name, target_path)
####################################################################################################
    # Functions that search the system for things
    def find_library(self, library):
        """ Search the system for a library, return its location if found otherwise return None."""
        command = "whereis " + library
        process = subprocess.Popen(args = command, shell = True, stdout=subprocess.PIPE)
        x, y = process.communicate()
        location = x.split( ':' )
        if len(location)==1:
            if location[0] == "\n" or location[0] == "":
                return None
            else:
                return location[0]
        else:
            if location[1] == "\n":
                return None
            else:
                return location[1]
    def library_exists(self, library, path):
        """ Check that the library exists in the path, will check correct extensions."""
        return os.path.exists(os.path.join(path, library + ".a")) or \
            os.path.exists(os.path.join(path, library + ".so")) or \
            os.path.exists(os.path.join(path, library + ".dylib"))
    def test_library(self, library, headers=[]):
        """ Test if code can be compiled with header and linked to libName."""
        return self._test_compile(headers, ["-l%s" % library])
    def test_framework_library(self, library, headers=[]):
        """ Test if code can be compiled with header and linked to libName for Mac OSX Frameworks."""
        return self._test_compile(headers, ["-framework","%s" % libName])
    def test_config(self, config, headers=[]):
        """ Test if code can be compiled using a xxx-config command."""
        libs = self.execute_command(config, ["--libs"]).strip('\n').split(' ')
        includes = self.execute_command(config, ["--includes"]).strip('\n').split(' ')
        return self._test_compile(headers, libs + includes)
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
            return True, output
        except !!
            os.remove( fileName )
            return False, e.Pipe

    def _check_clean_environment(self):
        """ Check the environment is clean (mainly no G4 variables)."""
        for envbit in os.environ:
            inenv = env[envbit].find('G4')
            if inenv!=-1:
                self._logger.Error!!
                raise !!
    def _build_path(self, path):
        """ Change the path into a global path and ensure the path exists."""
        globalPath = path
        if path[0] != '/': # Global path
            globalPath = os.path.abspath(os.path.join(os.getcwd(), path ))
        if not os.path.exists(globalPath):
            os.makedirs(globalPath)
        return globalPath
    def _serialise(path, data):
        """ Pickle data to path."""
        data_file = open(path, "w")
        pickle.dump(data, data_file)
        data_file.close()
    def _deserialise(path):
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
