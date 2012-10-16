#!/usr/bin/env python
#
# Gollum
#
# The gollum package installer
#
# Author P G Jones - 29/09/2012 <p.g.jones@qmul.ac.uk> : First revision
####################################################################################################
import conditionalpackage
import os

class Gollum(conditionalpackage.ConditionalPackage):
    """ Gollum install package."""
    def __init__(self, name, system):
        """ Initlaise the Gollum package."""
        super(Gollum, self).__init__(name, system)
    def get_dependencies(self):
        """ Return the dependencies."""
        return []
    def _is_system_installed(self):
        """ Check if installed on the system."""
        return self._system.find_library(self._name)
    def _is_downloaded(self):
        """ Nothing to do."""
        pass
    def _is_installed(self):
        """ Check if installed."""
        return self._system.file_exists("gollum", os.path.join(self.get_install_path(), "bin"))
    def _install(self):
        """ Install gollum via ruby gems."""
        self._system.execute_command("gem", 
                                     ["install", "gollum", "-i", self.get_install_path()])
    def remove(self):
        """ Must first uninstall via gems."""
        self._system.execute_command("gem", 
                                     ["uninstall", "gollum", "-x", "-i", self.get_install_path()])
        self._system.remove(self.get_install_path())
