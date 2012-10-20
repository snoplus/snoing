#!/usr/bin/env python
#
# RatTools
#
# Git clones rat-tools and installs the various sub projects
#
# Author P G Jones - 15/10/2012 <p.g.jones@qmul.ac.uk> : First revision
####################################################################################################
import localpackage
import os
import system
import getpass

class RatTools(localpackage.LocalPackage):
    """ Base class for rat-tools."""
    def __init__(self, name, system, root_dep, rat_dep):
        """ Initialise rat-tools."""
        self._root_dep = root_dep
        self._rat_dep = rat_dep
        super(RatTools, self).__init__(name, system)
    def _is_installed(self):
        """ RATZDAB wont install on macs."""
        if self._system.get_os_type() == system.System.Mac:
            return self._system.file_exists('README.md',self.get_install_path())
        else:
            return self._system.library_exists("libratzdab", os.path.join(self.get_install_path(), 
                                                                          "ratzdab", "lib"))
    def _install(self):
        """ Install RATZDAB, except on macs."""
        if self._system.get_os_type() == system.System.Mac:
            return True
        env = {"RATROOT" : self._dependency_paths[self._rat_dep],
               "ROOTSYS" : self._dependency_paths[self._root_dep],
               "LD_LIBRARY_PATH" : os.path.join(self._dependency_paths[self._root_dep], "lib"),
               "PATH" : os.path.join(self._dependency_paths[self._root_dep], "bin")}
        ratzdab_path = os.path.join(self.get_install_path(), "ratzdab")
        self._system.execute_command("make", [], ratzdab_path, env)
    def get_dependencies(self):
        """ Depends on rat-dev and root."""
        return [self._rat_dep, self._root_dep]

class RatToolsDevelopment(RatTools):
    '''RatTools development class'''
    def __init__(self, name, system, root_dep):
        """ Initialise rat-tools."""
        super(RatToolsDevelopment, self).__init__(name, system, root_dep, "rat-dev")
    def _download(self):
        """ Git clone rattools-dev."""
        self._system.execute_command("git", ["clone", "git@github.com:snoplus/rat-tools.git",
                                             self.get_install_path()],
                                     verbose=True)
    def _is_downloaded(self):
        """ Check if repo has been downloaded."""
        return os.path.exists(self.get_install_path())
    def _update(self):
        """ Special updater for rat-tools, just git pull then install again."""
        self._system.execute_command("git", ["pull"], cwd=self.get_install_path(), verbose=True)
        self._install()

class RatToolsRelease(RatTools):
    '''RatTools tagged/snapshot release'''
    def __init__(self, name, system, root_dep, rat_dep, tar_name):
        """ Initialise rat-tools."""
        super(RatToolsRelease, self).__init__(name, system, root_dep, rat_dep)
        self._tar_name = tar_name
    def _download(self):
        """ Download rat-tools snapshot."""
        if self._token is None and self._username is None:
            raise Exception("No username or token supplied for github authentication.")
        elif self._token is not None:
            self._system.download_file(
                "https://api.github.com/repos/snoplus/rat-tools/tarball/" + self._tar_name, 
                token = self._token)
        else:
            password = getpass.getpass("github password:")
            self._system.download_file(
                "https://github.com/snoplus/rat-tools/tarball/" + self._tar_name, self._username, password)
    def _is_downloaded(self):
        """ Check if tarball has been downloaded."""
        return self._system.file_exists(self._tar_name)
    def _install(self):
        """ Release installs must untar first."""
        self._system.untar_file(self._tar_name, self.get_install_path(), 1)
        super(RatToolsRelease, self)._install()
    def authenticate(self, username, token):
        """ Set the username or token  required for github downloads."""
        self._username = username
        self._token = token
    
