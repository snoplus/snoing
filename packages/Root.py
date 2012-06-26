#!/usr/bin/env python
# Author P G Jones - 12/05/2012 <p.g.jones@qmul.ac.uk> : First revision
# Author P G Jones - 13/05/2012 <p.g.jones@qmul.ac.uk> : Added 5.32, 5.28, 5.24 versions (rat v3, v2, v1)
#        O Wasalski - 13/06/2012 <wasalski@berkeley.edu> : Building python module
# The ROOT packages base class
import LocalPackage
import os
import PackageUtil

class Root( LocalPackage.LocalPackage ):
    """ Base root installer, different versions only have different names."""
    def __init__( self, name, tarName ):
        """ Initialise the root package."""
        super( Root, self ).__init__( name )
        self._TarName = tarName
        return
    # Functions to override
    def GetDependencies( self ):
        """ Return the dependency names as a list of names."""
        return [ "make", "g++", "gcc", "ld", "X11", "Xpm", "Xft", "Xext", "python" ]
    def _IsDownloaded( self ):
        """ Check the tar ball has been downloaded."""
        return os.path.exists( os.path.join( PackageUtil.kCachePath, self._TarName ) )
    def _IsInstalled( self ):
        """ Check if root is installed."""
        return os.path.exists( os.path.join( self.GetInstallPath(), "bin/root" ) )
    def _Download( self ):
        """ Derived classes should override this to download the package. Return True on success."""
        self._DownloadPipe += PackageUtil.DownloadFile( "ftp://root.cern.ch/root/" + self._TarName )
        return
    def _Install( self ):
        """ Derived classes should override this to install the package, should install only when finished. Return True on success."""
        self._InstallPipe += PackageUtil.UnTarFile( self._TarName, self.GetInstallPath(), 1 )
        self._InstallPipe += PackageUtil.ExecuteSimpleCommand( './configure', ['--enable-minuit2', '--enable-roofit',  '--enable-python','--with-x11-libdir=/usr/X11/lib','--with-xft-libdir=/usr/X11/lib','--with-xext-libdir=/usr/X11/lib'], None, self.GetInstallPath() )
        self._InstallPipe += PackageUtil.ExecuteSimpleCommand( 'make', [], None, self.GetInstallPath() )
        return
