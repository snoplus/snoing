#!/usr/bin/env python
# Author P G Jones - 22/06/2012 <p.g.jones@qmul.ac.uk> : First revision
# The Cmake conditional package
import ConditionalPackage
import PackageUtil
import os

class Cmake( ConditionalPackage.ConditionalPackage ):
    """ Cmake install package."""
    def __init__( self ):
        """ Initlaise the Cmake package."""
        super( Cmake, self ).__init__( "cmake" )
        return
    def CheckState( self ):
        """ Check if downloaded and installed."""
        # First test if globally installed
        if PackageUtil.FindLibrary( self._Name ) is not None: 
            # Now check the version
            versionString = PackageUtil.ExecuteSimpleCommand( "cmake", ["--version"], None, os.getcwd() ).split()[2]
            versionNumbers = versionString.split(".")
            if int( versionNumbers[0] ) >= 2 and int( versionNumbers[1] >= 8 ):
                # Installed is correct version
                self._SetMode( 2 )
                return
        # If here then must manually install
        if os.path.exists( os.path.join( PackageUtil.kCachePath, "cmake-2.8.8.tar.gz" ) ):
            self._SetMode( 1 ) # Downloaded
        if os.path.exists( os.path.join( self.GetInstallPath(), "bin/cmake" ) ):
            self._SetMode( 2 ) # Installed as well
        return
    def _Download( self ):
        """ Download the 2.8 version."""
        self._DownloadPipe += PackageUtil.DownloadFile( "http://www.cmake.org/files/v2.8/cmake-2.8.8.tar.gz")
        return
    def _Install( self ):
        """ Install the 2.8 version."""
        self._InstallPipe += PackageUtil.UnTarFile( "cmake-2.8.8.tar.gz", self.GetInstallPath(), 1 )
        self._InstallPipe += PackageUtil.ExecuteSimpleCommand( "./bootstrap", ["--prefix=%s" % self.GetInstallPath()], None, self.GetInstallPath() )
        self._InstallPipe += PackageUtil.ExecuteSimpleCommand( "make", [], None, self.GetInstallPath() )
        self._InstallPipe += PackageUtil.ExecuteSimpleCommand( "make", ["install"], None, self.GetInstallPath() )
        return
