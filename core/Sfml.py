#!/usr/bin/env python
# Author O Wasalski 
# OW - 07/06/2012 <wasalski@berkeley.edu> : First revision, new file
# The SFML packages base class
# Currently assumes all dependencies are installed on host machines
import LocalPackage
import os
import PackageUtil

class Sfml( LocalPackage.LocalPackage ):
    """ Base sfml installer package."""

    def __init__( self, name, revision = "" ):
        """ Initialise sfml with the tarName."""
        super( Sfml, self ).__init__( name )
        if( revision == "" ):
            revision = "master"
        self._URL = "https://github.com/LaurentGomila/SFML/tarball/" + revision
        return

########### "Public" functions - overrides LocalPackage ################

    def CheckState( self ):
        """ Check if downloaded and installed."""
        self._SetMode( 0 )
        if( self._Downloaded() ):
            self._SetMode( 1 )
        if( self._Installed() ):
            self._SetMode( 2 )

    def GetDependencies( self ):
        """ Return the required dependencies."""
        return []

########### "Private" functions - overrides LocalPackage ################

    def _Download( self ):
        """ Derived classes should override this to download the package. 
        Return True on success.""" 
        PackageUtil.DownloadFile( self._URL, fileName = self._Name )
        PackageUtil.UnTarFile( self._Name, self.GetInstallPath(), 1 )
        return self._Downloaded()

    def _Install( self ):
        """ Install the version."""
        env = os.environ
        installPath = self.GetInstallPath()

        PackageUtil.ExecuteSimpleCommand( \
            "cmake", [ "-DCMAKE_INSTALL_PREFIX:PATH=$PWD" ], env, installPath ) 

        PackageUtil.ExecuteSimpleCommand( "make", [], env, installPath )
        return self._Installed()

########### "Private" functions - helper for this class only ################

    def _Downloaded( self ):
        installPath = self.GetInstallPath()
        incfile = os.path.join( installPath, "include", "SFML", "System.hpp" )
        return os.path.isfile( incfile )

    def _Installed( self ):
        libDir = os.path.join( self.GetInstallPath(), "lib" )
        libs = [ "audio", "graphics", "network", "system", "window" ]
        result = True
        for lib in libs:
            libpath = os.path.join( libDir, "libsfml-" + lib + ".so" )
            result = result and os.path.isfile( libpath )
        return result



