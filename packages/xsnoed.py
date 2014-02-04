#!/usr/bin/env python
#
# Xsnoed, XsnoedRelease, XsnoedDevelopment
#
# Installers for xsnoed
#
# Author P G Jones - 2014-02-03 <p.g.jones@qmul.ac.uk> : First revision
####################################################################################################
import localpackage
import os
import getpass
import envfilebuilder

class Xsnoed(localpackage.LocalPackage):
    """ Base xsnoed installer for xsnoed."""
    def __init__(self, name, system, root_dep, geant_dep, rat_dep, rattools_dep):
        """ All Xsnoed installs have the same root and scons dependence."""
        super(Xsnoed, self).__init__(name, system)
        self._root_dep = root_dep
        self._geant_dep = geant_dep
        self._rat_dep = rat_dep
        self._rattools_dep = rattools_dep
    def get_dependencies(self):
        """ Return the dependency names as a list of names."""
        return [self._root_dep, self._geant_dep, self._rat_dep, self._rattools_dep, "Xm"]
    def _is_installed(self):
        """ Xsnoed releases and dev share a common install check."""
        # Check xsnoed
        sys = os.uname()[0]
        return self._system.file_exists('xsnoed', self.get_install_path())
    def _install(self):
        """ Install xsnoed, run configure then source environment and scons."""
        self.write_env_file()
        # Write the command file and source it...
        command_text = """#!/bin/bash\nsource %s\ncd %s\nmake""" % \
            (os.path.join(self._system.get_install_path(), "env_%s.sh" % self._name), 
             self.get_install_path())
        self._system.execute_complex_command(command_text)
    def _remove(self):
        """ Delete the env files as well."""
        self._system.remove(os.path.join(self._system.get_install_path(), "env_%s.sh" % self._name))
        self._system.remove(os.path.join(self._system.get_install_path(), "env_%s.csh" % self._name))
    def write_env_file(self):
        """ Adds general parts and then writes the env file."""
        self._env_file = envfilebuilder.EnvFileBuilder("#xsnoed environment\n")
        self._env_file.add_source(os.path.join(self._dependency_paths[self._root_dep], "bin"), "thisroot")
        self._env_file.add_source(os.path.join(self._dependency_paths[self._geant_dep], "bin"), "geant4")
        self._env_file.add_source(self._dependency_paths[self._rat_dep], "env")
        self._env_file.add_source(os.path.join(self._dependency_paths[self._rattools_dep], "ratzdab"), "env")
        self._env_file.write(self._system.get_install_path(), "env_%s" % self._name)

class XsnoedRelease(Xsnoed):
    """ Base xsnoed installer for xsnoed releases."""
    def __init__(self, name, system, root_dep, geant_dep, rat_dep, rattools_dep, tar_name):
        """ Initialise rat with the tar_name."""
        super(XsnoedRelease, self).__init__(name, system, root_dep, geant_dep, rat_dep, rattools_dep)
        self._download_name = tar_name
        self._tar_name = 'xsnoed_'+tar_name
    def _is_downloaded(self):
        """ Check if tarball has been downloaded."""
        return self._system.file_exists(self._tar_name)
    def _download(self):
        """ Derived classes should override this to download the package. Return True on success."""
        if self._token is None and self._username is None:
            raise Exception("No username or token supplied for github authentication.")
        elif self._token is not None:
            self._system.download_file(
                "https://api.github.com/repos/snoplus/xsnoed/tarball/" + self._download_name, 
                token = self._token, file_name = self._tar_name, retries = 3)
        else:
            password = getpass.getpass("github password:")
            self._system.download_file(
                "https://github.com/snoplus/xsnoed/tarball/" + self._download_name, self._username,
                password, file_name = self._tar_name, retries = 3)
    def _install(self):
        """ Release installs must untar first."""
        self._system.untar_file(self._tar_name, self.get_install_path(), 1)
        super(XsnoedRelease, self)._install()
    def authenticate(self, username, token):
        """ Set the username or token  required for github downloads."""
        self._username = username
        self._token = token

class XsnoedDevelopment(Xsnoed):
    """ Base xsnoed installer for xsnoed-dev."""
    def __init__(self, name, system):
        """ Initialise xsnoed with the tar_name."""
        super(XsnoedDevelopment, self).__init__(name, system, "root-5.34.11", "geant4.9.6.p02", 
                                             "rat-4.5.0", "rattools-4.5.0")
    def _is_downloaded(self):
        """ Check if tarball has been downloaded."""
        return os.path.exists(self.get_install_path())
    def _download(self):
        """ Git clone xsnoed-dev."""
        self._system.execute_command("git", ["clone", "git@github.com:snoplus/xsnoed.git", self.get_install_path()], 
                                     verbose=True)
    def _update(self):
        """ Special updater for xsnoed-dev, delete env file write a new then git pull and scons."""
        command_text = "#!/bin/bash\nsource %s\ncd %s\nmake clean" \
            % (os.path.join(self._system.get_install_path(), "env_%s.sh" % self._name), self.get_install_path())
        self._system.remove(os.path.join(self._system.get_install_path(), "env_%s.sh" % self._name))
        self._system.remove(os.path.join(self._system.get_install_path(), "env_%s.csh" % self._name))
        super(XsnoedDevelopment, self).write_env_file()
        command_text = "#!/bin/bash\nsource %s\ncd %s\nmake\n" \
            % (os.path.join(self._system.get_install_path(), "env_%s.sh" % self._name), self.get_install_path())
        self._system.execute_complex_command(command_text, verbose=True)
