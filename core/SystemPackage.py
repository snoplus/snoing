#!/usr/bin/env python
# Author P G Jones - 12/05/2012 <p.g.jones@qmul.ac.uk> : First revision
# Base class for packages that should be installed on the system and not by snoing.
# PHIL Should change to trial builds with linking, as is standard
import Package
import subprocess

class SystemPackage( Package.Package ):
    """ For referencing installed packages."""
    def __init__( self, name ):
        """ Initialise the package."""
        super( SystemPackage, self ).__init__( name )
        self._Mode = 0 # 0 is initial, 1 is installed
        return
    def IsInstalled( self ):
        """ Check and return if package is installed."""
        return self._Mode > 0
    # Functions to override
    def CheckState( self ):
        """ Derived classes should override this to ascertain the package status, downloaded? installed?"""
        return
    # Useful functions
    def _FindLibrary( self, libName ):
        """ Check if the library exists in the standard library locations. Return location if it does if not return None."""
        command = "whereis " + libName
        process = subprocess.Popen( args = command, shell = True, stdout=subprocess.PIPE)
        x, y = process.communicate()
        location = x.split( ':' )
        if location[1] == "\n":
            return None
        else:
            return location[1]
