#!/usr/bin/env python
# Author P G Jones - 15/05/2012 <p.g.jones@qmul.ac.uk> : First revision
# The GEANT4 packages base class
import LocalPackage
import os
import shutil

class Geant4Pre5( LocalPackage.LocalPackage ):
    """ Base geant4 installer for pre 4.9.5 geant versions."""
    def __init__( self, name, cachePath, installPath, graphical, sourceTar, dataTars, clhepDependency ):
        """ Initialise the geant4 package."""
        super( Geant4, self ).__init__( name, cachePath, installPath, graphical )
        self._InstallPath = os.path.join( self._InstallPath, name )
        self._SourceTar = sourceTar
        self._DataTars = dataTars
        self._ClhepDependency = clhepDependency
        return
    # Functions to override
    def CheckState( self ):
        """ Derived classes should override this to ascertain the package status, downloaded? installed?"""
        if os.path.exists( os.path.join( self._CachePath, self._TarName ) ):
            self._SetMode( 1 ) # Downloaded 
        if os.path.exists( os.path.join( self.GetInstallPath(), "lib" ) ):
            self._SetMode( 2 ) # Installed as well
        return
    def GetDependencies( self ):
        """ Return the dependency names as a list of names."""
        return [ "make", "g++", "gcc" ]
    def _Download( self ):
        """ Derived classes should override this to download the package."""
        self._DownloadFile( "http://geant4.web.cern.ch/geant4/support/source/" + self._SourceTar )
        for dataTar in self._DataTars:
            self._DownloadFile( "http://geant4.web.cern.ch/geant4/support/source/" + dataTar )
        return
    def _Install( self ):
        """ Derived classes should override this to install the package, should install only when finished. Return True on success."""
        # Geant4 is annoying must untar to somewhere then move and rename the subdirectory, grrr
        self._UnTarFile( self._TarName, "geant4-temp" )
        # If install path exists then clear (maybe this should be part of package?
        if os.path.exists( self.GetInstallPath() ):
            shutil.rmtree( self.GetInstallPath() )
        shutil.copytree( "geant4-temp/geant4", self.GetInstallPath() )
        shutil.rmtree( "geant4-temp" )
        # Now the data tars
        for dataTar in self._DataTars:
            self._UnTarFile( dataTar, os.path.join( self.GetInstallPath(), "data" ) )
        self._ExecuteCommand( './configure', ['-incflags -build -d -e -f'], None, self.GetInstallPath() )
        self._ExecuteCommand( './configure', ['-incflags -install -d -e -f '], None, self.GetInstallPath() )
        self._ExecuteCommand( './configure', [], None, self.GetInstallPath() )
        return True
    def WriteGeant4ConfigFile( self ):
        """ Return a dict of environment variables as relevant to geant4."""
        clhepPath = self._Dependencies[self._ClhepDependency]
        # Load existing in geant folder and replace...
