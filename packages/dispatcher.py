#!/usr/bin/env python
#
# Disp: Dispatcher for SNO+ data
#
# Git clones dispatcher and installs it
#
# Author K E Gilje - 06/09/2018 <gilje@ualberta.ca> : First revision
####################################################################################################
import localpackage
import os

class Dispatcher(localpackage.LocalPackage):
    """ Base class for dispatcher."""
    def __init__(self, name, system):
        """ Initialise dispatcher."""
        super(Dispatcher, self).__init__(name, system)
    def get_dependencies(self):
        """ No External Dependencies."""
        return []
    def _is_downloaded(self):
        """ Check if downloaded."""
        return os.path.exists(self.get_install_path())
    def _is_installed(self):
        return self._system.library_exists("libconthost", os.path.join(self.get_install_path(), 
                                                                       "lib"))
    def _download(self):
        """ Git clone dispatcher."""
        self._system.execute_command("git", ["clone", "https://github.com/snoplus/disp.git",
                                             self.get_install_path()],
                                     verbose=True)
    def _install(self):
        """ Install Dispatcher."""
        self._system.execute_command("make", [], self.get_install_path())
    def _update(self):
        """ Special updater for Dispatcher, just git pull then install again."""
        self._system.execute_command("git", ["pull"], cwd=self.get_install_path(), verbose=True)
        self._install()
