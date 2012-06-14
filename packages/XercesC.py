#!/usr/bin/env python
# Author P G Jones - 19/05/2012 <p.g.jones@qmul.ac.uk> : First revision
# The Xerces-c conditional package
import ConditionalPackage
import PackageUtil
import os

class XercesC( ConditionalPackage.ConditionalPackage ):
    """ XercesC install package."""
    def __init__( self ):
        """ Initlaise the XercesC packages."""
        super( XercesC, self ).__init__( "xerces-c-3.1.1", "xerces-c" )
        return
    def _CheckState( self ):
        """ Check if downloaded and installed."""
        if os.path.exists( os.path.join( PackageUtil.kCachePath, "xerces-c-3.1.1.tar.gz" ) ):
            self._SetMode( 1 ) # Downloaded
        if os.path.exists( os.path.join( self.GetInstallPath(), "lib/libxerces-c.a" ) ):
            self._SetMode( 2 ) # Installed as well
        return
    def _Download( self ):
        """ Download the 3.1.1 version."""
        self._DownloadPipe += PackageUtil.DownloadFile( "http://mirror.ox.ac.uk/sites/rsync.apache.org//xerces/c/3/sources/xerces-c-3.1.1.tar.gz" )
    def _Install( self ):
        """ Install the 3.1.1 version."""
        self._InstallPipe += PackageUtil.UnTarFile( "xerces-c-3.1.1.tar.gz", self.GetInstallPath(), 1 )
        self._InstallPipe += PackageUtil.ExecuteSimpleCommand( "./configure", [], None, self.GetInstallPath() )
        self._InstallPipe += PackageUtil.ExecuteSimpleCommand( "make", [], None, self.GetInstallPath() )
        self._InstallPipe += PackageUtil.ExecuteSimpleCommand( "make", ["install", "prefix=%s" % self.GetInstallPath()], None, self.GetInstallPath() )
        return 
