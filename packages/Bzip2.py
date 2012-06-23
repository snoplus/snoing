#!/usr/bin/env python
# Author O Wasalski - 13/06/2012 <wasalski@berkeley.edu> : First revision, new file
# Author P G Jones - 23/06/2012 <p.g.jones@qmul.ac.uk> : Refactor of Package Structure 
# The Bzip2 condiational Package
import ConditionalLibraryPackage
import os
import PackageUtil

class Bzip2( ConditionalLibraryPackage.ConditionalLibraryPackage ):
    """ Base bzip2 installer package."""
    def __init__( self, name, tarName ):
        """ Initialise bzip2 with the tarName."""
        super( Bzip2, self ).__init__( name, "bz2", "bzlib.h" )
        self._TarName = tarName
        return

    def GetDependencies( self ):
        """ Return the required dependencies."""
        return []
    def _IsDownloaded( self ):
        """ Has the tar file been downloaded."""
        return os.path.exists( os.path.join( PackageUtil.kCachePath, self._TarName ) )
    def _IsInstalled( self ):
        """ Has bzip2 been installed."""
        files = [os.path.join("bin", "bzip2"),
                 os.path.join("lib", "lib%s.a" %self._Library),
                 os.path.join("include", self._Header)]
        return PackageUtil.All( [os.path.isfile( os.path.join( self.GetInstallPath(), f ) ) for f in files] )
    def _Download( self ):
        """ Download the tar file."""
        self._DownloadPipe += PackageUtil.DownloadFile( "http://www.bzip.org/1.0.6/" + self._TarName )
        return
    def _Install( self ):
        """ Install bzip2."""
        PackageUtil.UnTarFile(self._TarName, self.GetInstallPath(), 1)
        self._InstallPipe += PackageUtil.ExecuteSimpleCommand("make", ["-f", "Makefile-libbz2_so"], None, self.GetInstallPath())
        self._InstallPipe += PackageUtil.ExecuteSimpleCommand("make", ["install", "PREFIX=" + self.GetInstallPath()], None, self.GetInstallPath())
        return
