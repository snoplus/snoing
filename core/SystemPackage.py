#!/usr/bin/env python
# Author P G Jones - 12/05/2012 <p.g.jones@qmul.ac.uk> : First revision
# Base class for packages that should be installed on the system and not by snoing.

class SystemPackage( object ):
    """ For referencing installed packages."""
    def __init__( self, name, cacheLocation ):
        """ Initialise the package."""
        self._Mode = 0 # Mode 0 is initial, 1 is installed
        self._Name = name
        return
    def IsInstalled( self ):
        """ Check and return if package is installed."""
        return self._Mode > 0
    # Functions to override
    def CheckState( self ):
        """ Derived classes should override this to ascertain the package status, downloaded? installed?"""
        return
    def GetInstallLocation( self ):
        """ Derived classes should override this."""
        return ""
