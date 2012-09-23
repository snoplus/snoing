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
# Author P G Jones - 23/09/2012 <p.g.jones@qmul.ac.uk> : Major refactor of snoing.
####################################################################################################
import localpackage
import os
import getpass
import envfilebuilder

class Rat(localpackage.LocalPackage):
    """ Base rat installer for rat."""
    def __init__(self, name, system, root_dep, scons_dep):
        """ All Rat installs have the same root and scons dependence."""
        super(Rat, self).__init__(name, system)
        self._env_file = envfilebuilder.EnvFileBuilder("#rat environment\n")
        self._root_dep = root_dep
        self._scons_dep = scons_dep
    def get_dependencies(self):
        """ Return the dependency names as a list of names."""
        dependencies = ["python", ["python-dev", "python-dev-2.4"], self._scons_dep, self._root_dep]
        dependencies.extend(self._get_dependencies())
        return dependencies
    def _is_downloaded(self):
        """ Check if downloaded, git-cloned or tar file downloaded."""
        pass
    def _is_installed(self):
        """ Rat releases and dev share a common install check."""
        # Check rat, root, RATLib and RATDSLib
        sys = os.uname()[0]
        return self._system.file_exists('rat_%s-g++' % sys, 
                                        os.path.join(self.get_install_path(), "bin")) \
            and self._system.file_exists('root', 
                                         os.path.join(self.get_install_path(), "bin")) \
            and self._system.library_exists("librat_%s-g++" % sys, 
                                            os.path.join(self.get_install_path(), "lib")) \
            and self._system.library_exists("libRATEvent_%s-g++" % sys, 
                                            os.path.join(self.get_install_path(), "lib"))
    def _download(self):
        """ Dependends on rat type."""
        pass
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
        os.remove(os.path.join(self._system.get_install_path(), "env_%s.sh" % self._name))
        os.remove(os.path.join(self._system.get_install_path(), "env_%s.csh" % self._name))
    def write_env_file(self):
        """ Adds general parts and then writes the env file."""
        self._env_file.add_environment("ROOTSYS", self._dependency_paths[self._root_dep])
        self._env_file.add_environment("RAT_SCONS", self._dependency_paths[self._scons_dep])
        self._env_file.append_path(os.path.join(self._dependency_paths[self._root_dep], "bin"))
        self._env_file.append_python_path(os.path.join(self._dependency_paths[self._root_dep], 
                                                       "lib"))
        self._env_file.append_library_path(os.path.join(self._dependency_paths[self._root_dep], 
                                                        "lib"))
        self._env_file.add_final_source(self.get_install_path(), "env")
        self._write_env_file()
        self._env_file.write_env_files(self._system.get_install_path(), "env_%s" % self._name)
    # Functions that must be implemented by sub classes
    def _write_env_file(self):
        """ Sub classes should add parts to the env file."""
        pass
    def _get_dependencies(self):
        """ Sub classes should return a list of dependencies."""
        pass

class RatRelease(Rat):
    """ Base rat installer for rat releases."""
    def __init__(self, name, system, root_dep, scons_dep, tar_name):
        """ Initialise rat with the tar_name."""
        super(RatRelease, self).__init__(name, system, root_dep, scons_dep)
        self._tar_name = tar_name
    def _is_downloaded(self):
        """ Check if tarball has been downloaded."""
        return self._system.file_exists(self._tar_name)
    def _download(self):
        """ Derived classes should override this to download the package. Return True on success."""
        if self._token is not None:
            self._system.download_file(
                "https://api.github.com/repos/snoplus/rat/tarball/" + self._tar_name, token = self._Token)
        else:
            print "Github password:"
            password = getpass.getpass()
            self._system.download_file(
                "https://github.com/snoplus/rat/tarball/" + self._tar_name, self._username, password)
    def _install(self):
        """ Release installs must untar first."""
        self._system.untar_file(self._tar_name, self.get_install_path(), 1)
        super(RatRelease, self)._install()
    def authenticate(self, username, token):
        """ Set the username or token  required for github downloads."""
        self._username = username
        self._token = token
