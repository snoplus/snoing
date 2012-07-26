#!/usr/bin/env python
# Author P G Jones - 12/05/2012 <p.g.jones@qmul.ac.uk> : First revision
# Author P G Jones - 23/06/2012 <p.g.jones@qmul.ac.uk> : Refactor of Package Structure
# Package installer base class
import Package
import os
import PackageUtil
import Log

class LocalPackage( Package.Package ):
    """ Base class for packages that can be installed."""
    def __init__( self, name, graphicalOnly = False ):
        """ Initialise the package, grab a lock."""
        super( LocalPackage, self ).__init__( name )
        self._Mode = 0 # Mode 0 is initial, 1 is post download, 2 is post install
        self._DependencyPaths = {}
        self._Graphical = graphicalOnly
        self._InstallPipe = "" # Install output
        self._DownloadPipe = "" # Download output
        self._InstallPath = os.path.join( PackageUtil.kInstallPath, self._Name )
        return
    def IsGraphicalOnly( self ):
        """ Return package graphical status."""
        return self._Graphical
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
    def Install( self ):
        """ Full install process."""
        self.CheckState()
        self.Download()
        if self._Graphical and not PackageUtil.kGraphical:
            raise PackageException( "Install Error", "Must be a graphical install." )
        if not self.IsInstalled():
            try:
                self._Install()
                self._SetMode(2)
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
                self._SetMode(1)
            except Exception:
                Log.Error( "Download error for %s" % self._Name )
                Log.Detail( self._DownloadPipe )
                raise
        return
    def CheckState( self ):
        """ Check if the package is downloaded and/or installed."""
        if self._IsDownloaded():
            self._SetMode(1)
        if self._IsInstalled():
            self._SetMode(2)
        return
    # Functions to override
    def GetDependencies( self ):
        """ Return the dependency names as a list of names."""
        pass
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
    # Useful functions
    def _SetMode( self, mode ):
        """ Function to safely set the mode."""
        self._Mode = mode
        return
