#!/usr/bin/env python
# Author P G Jones - 12/05/2012 <p.g.jones@qmul.ac.uk> : First revision
# Author P G Jones - 15/05/2012 <p.g.jones@qmul.ac.uk> : Restructure packages
# Author P G Jones - 19/05/2012 <p.g.jones@qmul.ac.uk> : Move useful functions into PackageUtil
# Author P G Jones - 23/06/2012 <p.g.jones@qmul.ac.uk> : Refactor of Package Structure
# Package information base class

class Package( object ):
    """ Base class for all packages."""
    def __init__( self, name ):
        """ Construct the package with name"""
        self._Name = name
        self._CheckPipe = "" # Checking output
        return
    def GetName( self ):
        """ Return the package name."""
        return self._Name
    # Functions to override by sublasses
    def CheckState( self ):
        """ Function to force the package to check what it's status is."""
        pass
    def IsInstalled( self ):
        """ Check and return if package is installed."""
        return False
