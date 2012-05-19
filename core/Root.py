#!/usr/bin/env python
# Author P G Jones - 12/05/2012 <p.g.jones@qmul.ac.uk> : First revision
# Author P G Jones - 13/05/2012 <p.g.jones@qmul.ac.uk> : Added 5.32, 5.28, 5.24 versions (rat v3, v2, v1)
# The ROOT packages base class
import LocalPackage
import os
import PackageUtil

class Root( LocalPackage.LocalPackage ):
    """ Base root installer, different versions only have different names."""
    def __init__( self, name, cachePath, installPath, tarName ):
        """ Initialise the root package."""
        super( Root, self ).__init__( name, cachePath, installPath, False )
        self._TarName = tarName
        return
    # Functions to override
    def CheckState( self ):
        """ Derived classes should override this to ascertain the package status, downloaded? installed?"""
        if os.path.exists( os.path.join( self._CachePath, self._TarName ) ):
            self._SetMode( 1 ) # Downloaded 
        if os.path.exists( os.path.join( self.GetInstallPath(), "bin/root" ) ):
            self._SetMode( 2 ) # Installed as well
        return
    def GetDependencies( self ):
        """ Return the dependency names as a list of names."""
        return [ "make", "g++", "gcc" ]
    def _Download( self ):
        """ Derived classes should override this to download the package. Return True on success."""
        return PackageUtil.DownloadFile( "ftp://root.cern.ch/root/" + self._TarName )
    def _Install( self ):
        """ Derived classes should override this to install the package, should install only when finished. Return True on success."""
        result = PackageUtil.UnTarFile( self._TarName, self.GetInstallPath(), 1 )
        result = result && PackageUtil.ExecuteSimpleCommand( './configure', ['--enable-minuit2', '--enable-roofit'], None, self.GetInstallPath() )
        result = result && ExecuteSimpleCommand( 'make', [], None, self.GetInstallPath() )
        return result
