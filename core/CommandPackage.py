#!/usr/bin/env python
# Author P G Jones - 13/05/2012 <p.g.jones@qmul.ac.uk> : First revision
# Takes care of packages that are simple commands such as make, assumes name is the command
import Package

class CommandPackage( Package.Package ):
    """ For packages that are simple commands such as make."""
    def __init__( self, name ):
        """ Initialise the package."""
        super( CommandPackage, self ).__init__( name )
        self._Mode = 0 # 0 is initial, 1 is installed
        return
    def IsInstalled( self ):
        """ Check and return if package is installed."""
        return self._Mode > 0
    def CheckState( self ):
        """ Derived classes should override this to ascertain the package status, downloaded? installed?"""
        if self._FindLibrary( self._Name ) == None:
            print "%s is not installed." % self._Name
        else:
            self._Mode = 1
        return
