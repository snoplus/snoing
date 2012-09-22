#!/usr/bin/env python
#
# CommandPackage
#
# System packages that are invoked by a command for example make. By convention the package 
# self._name is the command.
#
# Author P G Jones - 13/05/2012 <p.g.jones@qmul.ac.uk> : First revision
# Author P G Jones - 23/06/2012 <p.g.jones@qmul.ac.uk> : Refactor of Package Structure
# Author P G Jones - 23/06/2012 <p.g.jones@qmul.ac.uk> : Major refactor of snoing.
####################################################################################################
import systempackage

class CommandPackage(systempackage.SystemPackage):
    """ For packages that are simple commands such as make."""
    def __init__(self, name, system, help_text):
        """ Initialise the package."""
        super(CommandPackage, self).__init__(name, system, help_text)
        return
    def check_state(self):
        """ For a command package, merely need to test if the command exists."""
        location = self._system.find_library(self._name)
        if location is not None:
            self._installed = True
            self._install_path = location
        return
