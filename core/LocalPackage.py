#!/usr/bin/env python
# Author P G Jones - 12/05/2012 <p.g.jones@qmul.ac.uk> : First revision
# Package installer base class
import Package
import os
import PackageUtil
import Log

class LocalPackage( Package.Package ):
    """ Base class to install libraries."""
    def __init__( self, name, graphicalOnly = False ):
        """ Initialise the package, grab a lock."""
        super( LocalPackage, self ).__init__( name )
        self._Mode = 0 # Mode 0 is initial, 1 is post download, 2 is post install
        self._DependencyPaths = {}
        self._Graphical = graphicalOnly
        return
    def IsDownloaded( self ):
        """ Return package is downloaded."""
        return self._Mode > 0
    def IsInstalled( self ):
        """ Check and return if package is installed."""
        return self._Mode > 1
    def SetDependencyPaths( self, paths ):
        """ Set the dependency path dictionary."""
        self._DependencyPaths = paths
        return
    def GetInstallPath( self ):
        """ Return a local package install path."""
        return os.path.join( PackageUtil.kInstallPath, self._Name )
    def Install( self ):
        """ Full install process."""
        self.CheckState()
        self.Download()
        if self._Graphical and not PackageUtil.kGraphical:
            raise PackageException( "Install Error", "Must be a graphical install." )
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
    def GetDependencies( self ):
        """ Return the dependency names as a list of names."""
        return []
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
