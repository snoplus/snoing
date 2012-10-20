#!/usr/bin/env python
#
# Avalanche
#
# Git clones avalanche and installs it
#
# Author P G Jones - 17/10/2012 <p.g.jones@qmul.ac.uk> : First revision
####################################################################################################
import localpackage
import os

class Avalanche(localpackage.LocalPackage):
    """ Base class for avalanche."""
    def __init__(self, name, system, root_dep, curl_dep):
        """ Initialise avalanche."""
        self._root_dep = root_dep
        self._curl_dep = curl_dep
        super(Avalanche, self).__init__(name, system)
    def get_dependencies(self):
        """ Depends on rat-dev and root."""
        return ["rat-dev", "rattools-dev", self._root_dep, self._curl_dep]
    def _is_downloaded(self):
        """ Check if downloaded."""
        return os.path.exists(self.get_install_path())
    def _is_installed(self):
        return self._system.library_exists("libavalanche", os.path.join(self.get_install_path(), 
                                                                        "lib"))
    def _download(self):
        """ Git clone rat-dev."""
        self._system.execute_command("git", ["clone", "git@github.com:pgjones/avalanche.git", # Switch back to mastbaum soon...
                                             self.get_install_path()],
                                     verbose=True)
    def _install(self):
        """ Install Avalanche."""
        env = {"RATROOT" : self._dependency_paths["rat-dev"],
               "ROOTSYS" : self._dependency_paths[self._root_dep],
               "RATZDAB_ROOT" : os.path.join(self._dependency_paths["rattools-dev"], "ratzdab"),
               "PATH" : os.path.join(self._dependency_paths[self._root_dep], "bin") + ":" + 
               os.path.join(self._dependency_paths[self._curl_dep], "bin"),
               "LD_LIBRARY_PATH" : os.path.join(self._dependency_paths[self._root_dep], "lib")}
        self._system.execute_command("make", [], self.get_install_path(), env=env)
    def _update(self):
        """ Special updater for rat-tools, just git pull then install again."""
        self._system.execute_command("git", ["pull"], cwd=self.get_install_path(), verbose=True)
        self._install()
