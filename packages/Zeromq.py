#!/usr/bin/env python
# Author P G Jones - 19/05/2012 <p.g.jones@qmul.ac.uk> : First revision
# The ZMQ conditional package
import ConditionalLibraryPackage
import PackageUtil
import os
import shutil

class Zeromq( ConditionalLibraryPackage.ConditionalLibraryPackage ):
    """ Zeromq install package."""
    def __init__( self, name, tarName ):
        """ Initlaise the ZMQ packages."""
        super( Zeromq, self ).__init__( name, "zmq", "zmq.h" )
        self._TarName = tarName
        return
    
    def GetDependencies( self ):
        """ Return the dependencies."""
        return []
    def _IsDownloaded( self ):
        """ Check if tar ball is downloaded."""
        return os.path.exists( os.path.join( PackageUtil.kCachePath, self._TarName ) )
    def _IsInstalled( self ):
        return PackageUtil.LibraryExists( os.path.join( self.GetInstallPath(), "lib" ), "libzmq" )
    def _Download( self ):
        """ Download the 2.2 version."""
        self._DownloadPipe += PackageUtil.DownloadFile( "http://download.zeromq.org/" + self._TarName )
        return
    def _Install( self ):
        """ Install the 2.2 version."""
        sourcePath = os.path.join( PackageUtil.kInstallPath, "%s-source" % self._Name )
        self._InstallPipe += PackageUtil.UnTarFile( self._TarName, sourcePath, 1 )
        self._InstallPipe += PackageUtil.ExecuteSimpleCommand( "./configure", [], None, sourcePath )
        self._InstallPipe += PackageUtil.ExecuteSimpleCommand( "make", [], None, sourcePath )
        self._InstallPipe += PackageUtil.ExecuteSimpleCommand( "make", ["install", "prefix=%s" % self.GetInstallPath()], None, sourcePath )
        return
