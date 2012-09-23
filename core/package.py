#!/usr/bin/env python
#
# Package class
#
# Base class for all packages
#
# Author P G Jones - 12/05/2012 <p.g.jones@qmul.ac.uk> : First revision
# Author P G Jones - 15/05/2012 <p.g.jones@qmul.ac.uk> : Restructure packages
# Author P G Jones - 19/05/2012 <p.g.jones@qmul.ac.uk> : Move useful functions into PackageUtil
# Author P G Jones - 23/06/2012 <p.g.jones@qmul.ac.uk> : Refactor of Package Structure
# Author P G Jones - 23/06/2012 <p.g.jones@qmul.ac.uk> : Major refactor of snoing.
####################################################################################################

class Package( object ):
    """ Base class for all packages."""
    def __init__(self, name, system):
        """ Construct the package with a name and the system installation information."""
        self._name = name
        self._system = system
    def get_name(self):
        """ Return the package name."""
        return self._name
    # Functions to override by sublasses
    def is_installed(self):
        """ Check and return if package is installed."""
        return False
    def get_install_path(self):
        """ Return a the package installation path."""
        return self._install_path
    def check_state(self):
        """ Function to force the package to check what it's status is."""
        pass
