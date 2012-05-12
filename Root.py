#!/usr/bin/env python
# Author P G Jones - 12/05/2012 <p.g.jones@qmul.ac.uk> : First revision
# The ROOT packages (versions)
import Package
import os
import shutil

class ROOT53203( Package.Package ):
    """ Root 5.32.03, install package."""
    def __init__( self, cachePath, installPath ):
        """ Initiliase the root 5.32.00 package."""
        super( ROOT53203, self ).__init__( "root-5.32.00", cachePath, installPath )
        self._TarName = "root_v5.32.03.source.tar.gz"
        return
    # Functions to override
    def CheckState( self ):
        """ Derived classes should override this to ascertain the package status, downloaded? installed?"""
        if os.path.exists( os.path.join( self._CachePath, self._TarName ) ):
            self._SetMode( 1 ) # Downloaded 
        if os.path.exists( os.path.join( self.GetInstallPath(), "bin/root.exe" ) ):
            self._SetMode( 2 ) # Installed as well
        return
    def GetInstallPath( self ):
        """ Derived classes should override this."""
        return os.path.join( self._InstallPath, "root-5.32.03" )
    def GetDependencies( self ):
        """ Return the dependency names as a list of names."""
        return []
    def Download( self ):
        """ Derived classes should override this to download the package. Return True on success."""
        self._DownloadFile( "ftp://root.cern.ch/root/root_v5.32.03.source.tar.gz" )
        return
    def Install( self ):
        """ Derived classes should override this to install the package, should install only when finished. Return True on success."""
        # Root is annoying must untar to somewhere then move and rename the subdirectory, grrr
        self._UnTarFile( self._TarName, "root-temp" )
        # If install path exists then clear (maybe this should be part of package?
        if os.path.exists( self.GetInstallPath() ):
            shutil.rmtree( self.GetInstallPath() )
        shutil.copytree( "root-temp/root", self.GetInstallPath() )
        shutil.rmtree( "root-temp" )
        self._ExecuteCommand( './configure', ['--enable-minuit2', '--enable-roofit'], None, self.GetInstallPath() )
        self._ExecuteCommand( 'make', [], None, self.GetInstallPath() )
        return
