#!/usr/bin/env python
# Author P G Jones - 16/05/2012 <p.g.jones@qmul.ac.uk> : First revision
# The RAT packages base class
import LocalPackage
import os
import shutil

class Rat( LocalPackage.LocalPackage ):
    """ Base rat installer, different versions only have different names."""
    def __init__( self, name, cachePath, installPath, tarName ):
        """ Initialise the rat package."""
        super( Rat, self ).__init__( name, cachePath, installPath, False )
        self._InstallPath = os.path.join( self._InstallPath, name )
        self._TarName = tarName
        return
    # Functions to override
    def CheckState( self ):
        """ Derived classes should override this to ascertain the package status, downloaded? installed?"""
        if os.path.exists( os.path.join( self._CachePath, self._TarName ) ):
            self._SetMode( 1 ) # Downloaded 
        if os.path.exists( os.path.join( self.GetInstallPath(), "bin/rat" ) ):
            self._SetMode( 2 ) # Installed as well
        return
    def GetDependencies( self ):
        """ Return the dependency names as a list of names."""
        return self._LocalDependencies
    def _Download( self ):
        """ Derived classes should override this to download the package. Return True on success."""
        self._DownloadFile( "https://github.com/snoplus/rat/tarball/" + self._Name )
        return True
    def _Install( self ):
        """ Derived classes should override this to install the package, should install only when finished. Return True on success."""
        # Rat is annoying must untar to somewhere then move and rename the subdirectory, grrr
        ratTempDir = os.path.join( self._CachePath, "rat-temp" )
        self._UnTarFile( self._TarName, ratTempDir )
        # If install path exists then clear (maybe this should be part of package?
        if os.path.exists( self.GetInstallPath() ):
            shutil.rmtree( self.GetInstallPath() )
        ratFolderName = os.listdir( ratTempDir )
        shutil.copytree( os.path.join( ratTempDir, ratFolderName ), self.GetInstallPath() )
        shutil.rmtree( ratTempDir )

        self._ExecuteCommand( './configure', ['--enable-minuit2', '--enable-roofit'], None, self.GetInstallPath() )
        self._ExecuteCommand( 'make', [], None, self.GetInstallPath() )
        return True
    def _WriteEnvFile( self ):
        """ Write the environment file for rat."""
