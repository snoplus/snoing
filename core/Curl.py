#!/usr/bin/env python
# Author O. Wasalski - 04/06/2012 <wasalski@berkeley.edu> : First revision, new file
# Author P G Jones - 23/06/2012 <p.g.jones@qmul.ac.uk> : Refactor of Package Structure
import ConditionalLibraryPackage
import os
import PackageUtil

class Curl( ConditionalLibraryPackage.ConditionalLibraryPackage ):
    """ Base curl installer package. """
    def __init__( self, name, tarName ):
        super( Curl, self ).__init__( name, "curl", "curl/curl.h" )
        self._TarName = tarName
        return
########### "Private" functions - overrides ConditionalLibraryPackage ############
    def GetDependencies( self ):
        """ Return the dependency names as a list of names."""
        return ["uuid"]
    def _IsDownloaded():
        """ Check if package is downloaded."""
        return os.path.exists( os.path.join( PackageUtil.kCachePath, self._TarName ) )
    def _IsInstalled():
        """ Returns true if the header, library and binary files are in the proper location."""
        header = os.path.isfile( os.path.join( self.GetInstallPath(), "include", "curl", "curl.h" ) )
        lib = os.path.isfile( os.path.join( self.GetInstallPath(), "lib", "libcurl.a" ) )
        bin = os.path.isfile( os.path.join( self.GetInstallPath(), "bin", "curl" ) )
        config = os.path.isfile( os.path.join( self.GetInstallPath(), "bin", "curl-config" ) )
        return header and lib and bin and config
    def _Download( self ):
        """ Downloads a curl tarball from the curl website."""
        self._DownloadPipe += PackageUtil.DownloadFile( "http://curl.haxx.se/download/" + self._TarName )
        return
    def _Install( self ):
        """ Derived classes should override this to install the package, should install only when finished."""
        env = os.environ
        sourcePath = os.path.join( PackageUtil.kInstallPath, "%s-source" % self._Name )
        self._InstallPipe += PackageUtil.UnTarFile( self._TarName, sourcePath, 1 )
        self._InstallPipe += PackageUtil.ExecuteSimpleCommand( "./configure", [ "--prefix=%s" %( self.GetInstallPath() ) ], env, sourcePath )
        self._InstallPipe += PackageUtil.ExecuteSimpleCommand( "make", [], env, sourcePath )
        self._InstallPipe += PackageUtil.ExecuteSimpleCommand( "make", [ "install" ], env, sourcePath )
        return
