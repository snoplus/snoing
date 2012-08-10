#!/usr/bin/env python
# Author O Wasalski 
# OW - 07/06/2012 <wasalski@berkeley.edu> : First revision, new file
# Author P G Jones - 24/06/2012 <p.g.jones@qmul.ac.uk> : Refactor for new package types.
# Author P G Jones - 27/07/2012 <p.g.jones@qmul.ac.uk> : Added snogoggles versions.
# The SNOGoggles packages
import Snogoggles
import os
import PackageUtil

class SnogogglesDev( Snogoggles.Snogoggles ):
    """ Installs development version. """
    def __init__( self ):
        """ Initializes snogoggles package. """
        super( SnogogglesDev, self ).__init__( "snogoggles-dev", "scons-2.1.0", "geant4.9.5.p01", "clhep-2.1.1.0", "rat-dev", "root-5.32.03", "sfml-2.0-rc", "xerces-c-3.1.1", "avalanche-1", "zeromq-2.2.0", "curl-7.26.0", "bzip2-1.0.6" )
        return
    def _IsDownloaded( self ):
        """ Check if downloaded."""
        return os.path.exists( self.GetInstallPath() )
    def _Download( self ):
        """ Download snogoggles (git clone)."""
        self._DownloadPipe += PackageUtil.ExecuteSimpleCommand( "git", ["clone", "git@github.com:snoplus/snogoggles.git",  \
                                                                            self.GetInstallPath()], None, os.getcwd(), True ) # Force verbose
        return
    def _WriteEnvFile( self ):
        """ Previous releases had a special geant4 environment, this justs needs to source the geant4.9.5 env"""
        self._EnvFile.AddSource( self._DependencyPaths[self._Geant4Dependency], "bin/geant4" )
        self._EnvFile.AddSource( self._DependencyPaths[self._RatDependency], "env" )
        return
    # Dev packages have special updates
    def _Update( self ):
        """ Special updater for rat-dev, delete env file write a new then git pull and scons."""
        os.remove( os.path.join( PackageUtil.kInstallPath, "env_%s.sh" % self._Name ) )
        os.remove( os.path.join( PackageUtil.kInstallPath, "env_%s.csh" % self._Name ) )
        self.WriteEnvFile()
        commandText = """#!/bin/bash\nsource %s\ncd %s\ngit pull\nscons -c\nscons""" % ( os.path.join( PackageUtil.kInstallPath, "env_%s.sh" % self._Name ), self.GetInstallPath() )
        self._InstallPipe += PackageUtil.ExecuteComplexCommand( commandText, True )
        return

class SnogogglesAirFill( Snogoggles.SnogogglesRelease ):
    """ Installs the air fill (1) version."""
    def __init__( self ):
        super( SnogogglesAirFill, self ).__init__( "snogoggles-airfill", "604ae90e913586360779f96035bbab6c4709964f", "scons-2.1.0", "geant4.9.4.p01", "clhep-2.1.0.1", "rat-3", "root-5.32.03", "sfml-1.8", "xerces-c-3.1.1", "avalanche-1", "zeromq-2.2.0", "curl-7.26.0", "bzip2-1.0.6" )
        return
