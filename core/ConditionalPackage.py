#!/usr/bin/env python
# Author P G Jones - 19/05/2012 <p.g.jones@qmul.ac.uk> : First revision
# Conditional package, checks if installed on the system. If not installs locally e.g. curl.
import Package
import os
import PackageUtil
import Log

class ConditionalPackage( Package.Package ):
    """ Base class to install libraries."""
    def __init__( self, name ):
        """ Initialise the package, grab a lock."""
        super( ConditionalPackage, self ).__init__( name )
        self._Mode = 0 # Mode 0 is initial, 1 is post download, 2 is post install
        self._InstallPath = None
        return
    def IsDownloaded( self ):
        """ Return package is downloaded."""
        return self._Mode > 0
    def IsInstalled( self ):
        """ Check and return if package is installed."""
        return self._Mode > 1
    def GetInstallPath( self ):
        """ Return a local package install path."""
        return self._InstallPath
    def Install( self ):
        """ Full install process."""
        self.CheckState()
        self.Download()
        if not self.IsInstalled():
            try:
                self._Install()
                self._IncrementMode()
            except Exception:
                Log.Error( "Install error for %s" % self._Name )
                Log.Detail( self._InstallPipe )
                raise
    def Download( self ):
        """ Full download process."""
        self.CheckState()
        if not self.IsDownloaded():
            try:
                self._Download()
                self._IncrementMode()
            except Exception:
                Log.Error( "Download error for %s" % self._Name )
                Log.Detail( self._DownloadPipe )
                raise
        return
    # Functions to override
    def CheckState( self ):
        """ Derived classes should override this to ascertain the package status, downloaded? installed?"""
        return
    def _Download( self ):
        """ Derived classes should override this to download the package. Return True on success."""
        return False
    def _Install( self ):
        """ Derived classes should override this to install the package, should install only when finished. Return True on success."""
        return False
    # Useful functions
    def _IncrementMode( self ):
        """ Function to safely update the mode."""
        self._Mode += 1
        return
    def _SetMode( self, mode ):
        """ Function to safely set the mode."""
        self._Mode = mode
        return
