#!/usr/bin/env python
#
# Rat, RatRelease
#
# Installers for rat 
#
# Author P G Jones - 16/05/2012 <p.g.jones@qmul.ac.uk> : First revision
#        O Wasalski - 05/06/2012 <wasalski@berkeley.edu> : Added curl dependency to RatReleasePost3
#        P G Jones - 21/06/2012 <p.g.jones@qmul.ac.uk> : Second revision use env file builder, 
#                                                        refactored versions
#        P G Jones - 23/09/2012 <p.g.jones@qmul.ac.uk> : Major refactor of snoing.
####################################################################################################
import localpackage
import os
import getpass
import envfilebuilder

class Rat(localpackage.LocalPackage):
    """ Base rat installer for rat."""
    def __init__(self, name, system, root_dep, geant_dep, scons_dep):
        """ All Rat installs have the same root and scons dependence."""
        super(Rat, self).__init__(name, system)
        self._root_dep = root_dep
        self._scons_dep = scons_dep
        self._geant_dep = geant_dep
    def get_dependencies(self):
        """ Return the dependency names as a list of names."""
        dependencies = ["python", ["python-dev", "python-dev-2.4", "python-dev-2.6"],
                        self._geant_dep, self._scons_dep, self._root_dep]
        dependencies.extend(self._get_dependencies())
        return dependencies
    def _is_installed(self):
        """ Rat releases and dev share a common install check."""
        # Check rat, root, RATLib and RATDSLib
        sys = os.uname()[0]
        return self._system.file_exists('rat_%s' % sys, 
                                        os.path.join(self.get_install_path(), "bin")) \
               and self._system.file_exists('root', 
                                            os.path.join(self.get_install_path(), "bin")) \
               and self._system.library_exists("librat_%s" % sys, 
                                               os.path.join(self.get_install_path(), "lib")) \
               and self._system.library_exists("libRATEvent_%s" % sys, 
                                               os.path.join(self.get_install_path(), "lib"))
    def _install(self):
        """ Install rat, run configure then source environment and scons."""
        self.write_env_file()
        # Write the command file and source it...
        command_text = """#!/bin/bash\nsource %s\ncd %s\n./configure\nsource env.sh\nscons""" % \
            (os.path.join(self._system.get_install_path(), "env_%s.sh" % self._name), 
             self.get_install_path())
        self._system.execute_complex_command(command_text)
    def _remove(self):
        """ Delete the env files as well."""
        self._system.remove(os.path.join(self._system.get_install_path(), "env_%s.sh" % self._name))
        self._system.remove(os.path.join(self._system.get_install_path(), "env_%s.csh" % self._name))
    def write_env_file(self):
        """ Adds general parts and then writes the env file."""
        self._env_file = envfilebuilder.EnvFileBuilder("#rat environment\n")
        self._env_file.add_environment("ROOTSYS", self._dependency_paths[self._root_dep])
        self._env_file.add_environment("RAT_SCONS", self._dependency_paths[self._scons_dep])
        self._env_file.append_path(os.path.join(self._dependency_paths[self._root_dep], "bin"))
        self._env_file.append_python_path(os.path.join(self._dependency_paths[self._root_dep], 
                                                       "lib"))
        self._env_file.append_library_path(os.path.join(self._dependency_paths[self._root_dep], 
                                                        "lib"))
        self._env_file.add_post_source(self.get_install_path(), "env")
        self._write_env_file()
        self._env_file.write(self._system.get_install_path(), "env_%s" % self._name)
    # Functions that must be implemented by sub classes
    def _write_env_file(self):
        """ Sub classes should add parts to the env file."""
        pass
    def _get_dependencies(self):
        """ Sub classes should return a list of dependencies."""
        pass

class RatRelease(Rat):
    """ Base rat installer for rat releases."""
    def __init__(self, name, system, root_dep, geant_dep, scons_dep, tar_name):
        """ Initialise rat with the tar_name."""
        super(RatRelease, self).__init__(name, system, root_dep, geant_dep, scons_dep)
        self._download_name = tar_name
        self._tar_name = 'rat_'+tar_name
    def _is_downloaded(self):
        """ Check if tarball has been downloaded."""
        return self._system.file_exists(self._tar_name)
    def _download(self):
        """ Derived classes should override this to download the package. Return True on success."""
        if self._token is None and self._username is None:
            raise Exception("No username or token supplied for github authentication.")
        elif self._token is not None:
            self._system.download_file(
                "https://api.github.com/repos/snoplus/rat/tarball/" + self._download_name, 
                token = self._token, file_name = self._tar_name, retries = 3)
        else:
            password = getpass.getpass("github password:")
            self._system.download_file(
                "https://github.com/snoplus/rat/tarball/" + self._download_name, self._username,
                password, file_name = self._tar_name, retries = 3)
    def _install(self):
        """ Release installs must untar first."""
        self._system.untar_file(self._tar_name, self.get_install_path(), 1)
        super(RatRelease, self)._install()
    def authenticate(self, username, token):
        """ Set the username or token  required for github downloads."""
        self._username = username
        self._token = token

class RatDevelopment(Rat):
    """ Base rat installer for rat-dev."""
    def __init__(self, name, system):
        """ Initialise rat with the tar_name."""
        super(RatDevelopment, self).__init__(name, system, "root-5.34.21", "geant4.10.0.p02", "scons-2.1.0")
    def _get_dependencies(self):
        """ Return the extra dependencies."""
        return ["curl-7.26.0", "bzip2-1.0.6"]
    def _is_downloaded(self):
        """ Check if tarball has been downloaded."""
        return os.path.exists(self.get_install_path())
    def _download(self):
        """ Git clone rat-dev."""
        self._system.execute_command("git", ["clone", "git@github.com:snoplus/rat.git", self.get_install_path()], 
                                     verbose=True)
    def _write_env_file(self):
        """ Write the environment file required for the current rat-dev."""
        self._env_file.add_source(self._dependency_paths[self._geant_dep], "bin/geant4")
        self._env_file.append_path(os.path.join(self._dependency_paths[self._geant_dep], "bin"))
        if self._dependency_paths["curl-7.26.0"] is not None: # Conditional Package
            self._env_file.append_path(os.path.join(self._dependency_paths["curl-7.26.0"], "bin"))
            self._env_file.append_library_path(os.path.join(self._dependency_paths["curl-7.26.0"], "lib"))
        if self._dependency_paths["bzip2-1.0.6"] is not None: # Conditional Package
            self._env_file.add_environment("BZIPROOT", self._dependency_paths["bzip2-1.0.6"])
            self._env_file.append_library_path(os.path.join(self._dependency_paths["bzip2-1.0.6"], "lib"))
    def _update(self):
        """ Special updater for rat-dev, delete env file write a new then git pull and scons."""
        command_text = "#!/bin/bash\nsource %s\ncd %s\nscons -c" \
            % (os.path.join(self._system.get_install_path(), "env_%s.sh" % self._name), self.get_install_path())
        self._system.remove(os.path.join(self._system.get_install_path(), "env_%s.sh" % self._name))
        self._system.remove(os.path.join(self._system.get_install_path(), "env_%s.csh" % self._name))
        super(RatDevelopment, self).write_env_file()
        command_text = "#!/bin/bash\nsource %s\ncd %s\ngit pull\n./configure\n" \
            % (os.path.join(self._system.get_install_path(), "env_%s.sh" % self._name), self.get_install_path())
        self._system.execute_complex_command(command_text, verbose=True)
        command_text = "#!/bin/bash\nsource %s\ncd %s\nscons\n" \
            % (os.path.join(self._system.get_install_path(), "env_%s.sh" % self._name), self.get_install_path())
        self._system.execute_complex_command(command_text, verbose=True)
