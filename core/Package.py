#!/usr/bin/env python
# Author P G Jones - 12/05/2012 <p.g.jones@qmul.ac.uk> : First revision
# Author P G Jones - 15/05/2012 <p.g.jones@qmul.ac.uk> : Restructure packages
# Author P G Jones - 19/05/2012 <p.g.jones@qmul.ac.uk> : Move useful functions into PackageUtil
# Package information base class

class Package( object ):
    """ Base class to install libraries."""
    def __init__( self, name ):
        """ Construct the package with name"""
        self._Name = name
        self._InstallPath = None # Location where the package is installed
        self._InstallPipe = "" # Install output
        self._DownloadPipe = "" # Download output
        return
    def GetName( self ):
        """ Return the package name."""
        return self._Name
    def GetInstallPath( self ):
        """ Return the package install location."""
        return self._InstallPath
    # Functions to override
    def CheckState( self ):
        """ Function to force the package to check what it's status is."""
        return
    def IsInstalled( self ):
        """ Check and return if package is installed."""
        return False
