#!/usr/bin/env python
#
# SystemPackage
#
# For packages that cannot be installed by snoing (system libraries etc...), but should be present 
# on the system.
#
# Author P G Jones - 23/06/2012 <p.g.jones@qmul.ac.uk> : First Revision
# Author P G Jones - 23/06/2012 <p.g.jones@qmul.ac.uk> : Major refactor of snoing.
####################################################################################################
import package

class SystemPackage( package.Package ):
    """ Base class for system wide packages."""
    def __init__(self, name, system, help_text):
        """ Construct with help text (which should be a hint to the user about what to install on 
        the system).
        """
        super(SystemPackage, self).__init__(name,system)
        self._help_text = help_text
        self._installed = False
        return
    def get_help_text(self):
        """ Return the package help text."""
        return self._help_text
    def is_installed(self):
        """ Check and return if package is installed."""
        return self._installed
    # Functions to override by sublasses
    def check_state(self):
        """ Function to force the package to check what it's status is."""
        pass
