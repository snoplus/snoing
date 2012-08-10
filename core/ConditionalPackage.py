#!/usr/bin/env python
# Author P G Jones - 19/05/2012 <p.g.jones@qmul.ac.uk> : First revision
# Author P G Jones - 23/06/2012 <p.g.jones@qmul.ac.uk> : Refactor of Package Structure
# Conditional package, checks if installed on the system. If not installs locally e.g. cmake.
import LocalPackage
import os
import PackageUtil
import Log

class ConditionalPackage( LocalPackage.LocalPackage ):
    """ Base class to install libraries."""
    def __init__( self, name ):
        """ Initialise the package, grab a lock."""
        super( ConditionalPackage, self ).__init__( name, False ) # Conditional Packages cannot be graphical
        self._InstallPath = None # Override install path to be None unless locally installed.
        return
    def CheckState( self ):
        """ Override the LocalPackage CheckState to check if package is system wide installed, 
        if not check download and install state."""
        if self._IsSystemInstalled():
            self._SetMode(2)
        else:
            # First set the correct install path then check
            self._InstallPath = os.path.join( PackageUtil.kInstallPath, self._Name )
            if self._IsDownloaded():
                self._SetMode(1)
            if self._IsInstalled():
                self._SetMode(2)
        return        
    def Update( self ):
        """ Update the package install, usually deletes and reinstalls..."""
        self.CheckState()
        if self._Graphical and not PackageUtil.kGraphical:
            raise Exceptions.PackageException( "Install Error", "Must be a graphical install." )
        if self._IsSystemInstalled():
            self._SetMode(3)
            return
        if not self.IsInstalled():
            self.Install()
        else:
            self._Update()
            self._SetMode(3)
        return
    # Functions to override
    def GetDependencies( self ):
        """ Return the dependency names as a list of names."""
        pass
    def _IsSystemInstalled( self ):
        """ Check if package is installed on the system."""
        return False
    def _IsDownloaded( self ):
        """ Check if package is downloaded."""
        return False
    def _IsInstalled( self ):
        """ Check if package is installed."""
        return False
    def _Download( self ):
        """ Derived classes should override this to download the package.."""
        pass
    def _Install( self ):
        """ Derived classes should override this to install the package, should install only when finished."""
        pass
