#!/usr/bin/env python
# Author P G Jones - 19/05/2012 <p.g.jones@qmul.ac.uk> : First revision
# The Xerces-c conditional package
import ConditionalLibraryPackage
import PackageUtil
import os

class XercesC( ConditionalLibraryPackage.ConditionalLibraryPackage ):
    """ XercesC install package."""
    def __init__( self, name, tarName ):
        """ Initlaise the XercesC packages."""
        super( XercesC, self ).__init__( name, "xerces-c" )
        self._TarName = tarName
        return

    def GetDependencies( self ):
        """ Return the dependencies."""
        return ["curl-7.26.0"]
    def _IsDownloaded( self ):
        """ Check if the tar ball has been downloaded."""
        return os.path.exists( os.path.join( PackageUtil.kCachePath, self._TarName ) )
    def _IsInstalled( self ):
        """ Check if xercesc installed."""
        return os.path.exists( os.path.join( self.GetInstallPath(), "lib/libxerces-c.a" ) )
    def _Download( self ):
        """ Download the 3.1.1 version."""
        self._DownloadPipe += PackageUtil.DownloadFile( "http://mirror.ox.ac.uk/sites/rsync.apache.org//xerces/c/3/sources/" + self._TarName )
        return
    def _Install( self ):
        """ Install the 3.1.1 version."""
        sourcePath = os.path.join( PackageUtil.kInstallPath, "%s-source" % self._Name )
        self._InstallPipe += PackageUtil.UnTarFile( self._TarName, sourcePath, 1 )
        self._InstallPipe += PackageUtil.ExecuteSimpleCommand( "./configure", [], None, sourcePath )
        self._InstallPipe += PackageUtil.ExecuteSimpleCommand( "make", [], None, sourcePath )
        self._InstallPipe += PackageUtil.ExecuteSimpleCommand( "make", ["install", "prefix=%s" % self.GetInstallPath()], None, sourcePath )
        return 
