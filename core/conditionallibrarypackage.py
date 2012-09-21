#!/usr/bin/env python
#
# ConditionalLibraryPackage
#
# Checks if the library is on the system and if not allows installation
#
# Author P G Jones - 20/06/2012 <p.g.jones@qmul.ac.uk> : First revision
# Author P G Jones - 23/06/2012 <p.g.jones@qmul.ac.uk> : Refactor of Package Structure
# Author P G Jones - 23/06/2012 <p.g.jones@qmul.ac.uk> : Major refactor of snoing.
####################################################################################################
import conditionalpackage

class ConditionalLibraryPackage(conditionalpackage.ConditionalPackage):
    """ Base class to install conditional libraries."""
    def __init__(self, name, system, library, header = None):
        """ Initialise the with the library and header file (optional)."""
        super(ConditionalLibraryPackage, self).__init__(name, system)
        self._library = library
        self._header = header
        return
    def _is_system_installed( self ):
        """ Check if library is available on the system."""
        installed, output = self._system.PackageUtil.TestLibrary( self._Library, self._Header )
        self._check_pipe += output
        return installed
