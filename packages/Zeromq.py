#!/usr/bin/env python
# Author P G Jones - 19/05/2012 <p.g.jones@qmul.ac.uk> : First revision
# The ZMQ conditional package
import ConditionalPackage
import PackageUtil
import os
import shutil

class Zeromq( ConditionalPackage.ConditionalPackage ):
    """ Zeromq install package."""
    def __init__( self ):
        """ Initlaise the ZMQ packages."""
        super( Zeromq, self ).__init__( "zeromq-2.2.0", "zmq", "zmq.h" )
        return
    def _CheckState( self ):
        """ Check if downloaded and installed."""
        if os.path.exists( os.path.join( PackageUtil.kCachePath, "zeromq-2.2.0.tar.gz" ) ):
            self._SetMode( 1 ) # Downloaded
        if os.path.exists( os.path.join( self.GetInstallPath(), "lib/libzmq.a" ) ):
            self._SetMode( 2 ) # Installed as well
        return
    def _Download( self ):
        """ Download the 2.2 version."""
        self._DownloadPipe += PackageUtil.DownloadFile( "http://download.zeromq.org/zeromq-2.2.0.tar.gz" )
        return
    def _Install( self ):
        """ Install the 2.2 version."""
        sourcePath = os.path.join( PackageUtil.kInstallPath, "%s-source" % self._Name )
        self._InstallPipe += PackageUtil.UnTarFile( "zeromq-2.2.0.tar.gz", sourcePath, 1 )
        self._InstallPipe += PackageUtil.ExecuteSimpleCommand( "./configure", [], None, sourcePath )
        self._InstallPipe += PackageUtil.ExecuteSimpleCommand( "make", [], None, sourcePath )
        self._InstallPipe += PackageUtil.ExecuteSimpleCommand( "make", ["install", "prefix=%s" % self.GetInstallPath()], None, sourcePath )
        return
