#!/usr/bin/env python
# Author P G Jones - 19/05/2012 <p.g.jones@qmul.ac.uk> : First revision
# Author P G Jones - 23/06/2012 <p.g.jones@qmul.ac.uk> : Refactor of Package Structure
# Takes care of packages that are system installed libraries e.g. X11
import SystemPackage
import PackageUtil

class LibraryPackage( SystemPackage.SystemPackage ):
    """ For packages that are system wide libraries e.g. X11."""
    def __init__( self, name, helpText, libName, header = None ):
        """ Initialise the package."""
        super( LibraryPackage, self ).__init__( name, helpText )
        self._LibName = libName
        self._Header = header
        return
    def CheckState( self ):
        """ Need to test the library linking and inclusion of the header."""
        installed, self._CheckPipe = PackageUtil.TestLibrary( self._LibName, self._Header )
        if installed:
            self._Installed = True
        return
