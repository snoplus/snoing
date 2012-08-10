#!/usr/bin/env python
# Author P G Jones - 18/05/2012 <p.g.jones@qmul.ac.uk> : First revision
#        O Wasalski - 05/06/2012 <wasalski@berkeley.edu> : Added curl dependency to RAT-dev and rat-3
#        O Wasalski - 13/06/2012 <waslski@berkeley.edu> : Added bzip2 dependency to rat-dev
#        P G Jones - 21/06/2012 <p.g.jones@qmul.ac.uk> : New releases usage.
#        P G Jones - 02/08/2012 <p.g.jones@qmul.ac.uk> : Moved rat-dev to geant4.9.5 and updated rat-4
# The RAT packages (versions)
import Rat
import RatReleases
import os
import PackageUtil
import getpass #Temp RAT-4

class RATDev( Rat.Rat ):
    """ Rat dev install package."""
    def __init__( self ):
        """ Initiliase the rat dev package."""
        self._GeantDependency = "geant4.9.5.p01"
        self._ClhepDependency = "clhep-2.1.1.0"
        self._CurlDependency = "curl-7.26.0"
        self._BzipDependency = "bzip2-1.0.6"
        self._AvalancheDependency = "avalanche-1"
        self._ZeromqDependency = "zeromq-2.2.0"
        self._XercescDependency = "xerces-c-3.1.1"
        super( RATDev, self ).__init__( "rat-dev", "root-5.32.03", "scons-2.1.0" )
        return
    def _GetDependencies( self ):
        """ Return the extra dependencies."""
        return [ self._GeantDependency, self._ClhepDependency, self._CurlDependency, self._BzipDependency, self._AvalancheDependency, \
                     self._ZeromqDependency, self._XercescDependency ]
    def _IsDownloaded( self ):
        """ Check if git clone has completed."""
        return os.path.exists( self.GetInstallPath() )
    def _Download( self ):
        """ Git clone rat-dev."""
        self._DownloadPipe += PackageUtil.ExecuteSimpleCommand( "git", ["clone", "git@github.com:snoplus/rat.git",  self.GetInstallPath()], None, os.getcwd(), True ) # Force verbose
        return
    def _WriteEnvFile( self ):
        """ Diff geant env file and no need to patch rat."""
        self._EnvFile.AddSource( self._DependencyPaths[self._GeantDependency], "bin/geant4" )
        self._EnvFile.AppendLibraryPath( os.path.join( self._DependencyPaths[self._ClhepDependency], "lib" ) )
        self._EnvFile.AddEnvironment( "AVALANCHEROOT", self._DependencyPaths[self._AvalancheDependency] )
        if self._DependencyPaths[self._ZeromqDependency] is not None: # Conditional Package, set to None if installed on system instead of locally
            self._EnvFile.AddEnvironment( "ZEROMQROOT", self._DependencyPaths[self._ZeromqDependency] )
        if self._DependencyPaths[self._XercescDependency] is not None: # Conditional Package, set to None if installed on system instead of locally
            self._EnvFile.AddEnvironment( "XERCESCROOT", self._DependencyPaths[self._XercescDependency] )
        self._EnvFile.AppendPath( os.path.join( self._DependencyPaths[self._ClhepDependency], "bin" ) )
        self._EnvFile.AppendPath( os.path.join(self._DependencyPaths[self._GeantDependency], "bin" ) )
        self._EnvFile.AppendLibraryPath( os.path.join( self._DependencyPaths[self._ClhepDependency], "lib" ) )
        self._EnvFile.AppendLibraryPath( os.path.join( self._DependencyPaths[self._AvalancheDependency], "lib/cpp" ) )
        self._EnvFile.AppendLibraryPath( os.path.join( self._DependencyPaths[self._ZeromqDependency], "lib" ) )
        self._EnvFile.AppendLibraryPath( os.path.join( self._DependencyPaths[self._XercescDependency], "lib" ) )
        if self._DependencyPaths[self._CurlDependency] is not None: # Conditional Package, set to None if installed on system instead of locally
            self._EnvFile.AppendPath( os.path.join( self._DependencyPaths[self._CurlDependency], "bin" ) )
        if self._DependencyPaths[self._BzipDependency] is not None: # Conditional Package, set to None if installed on system instead of locally
            self._EnvFile.AddEnvironment( "BZIPROOT", self._DependencyPaths[self._BzipDependency] )
            self._EnvFile.AppendLibraryPath( os.path.join( self._DependencyPaths[self._BzipDependency], "lib" ) )
        return
    # Dev packages have special updates
    def _Update( self ):
        """ Special updater for rat-dev, delete env file write a new then git pull and scons."""
        os.remove( os.path.join( PackageUtil.kInstallPath, "env_%s.sh" % self._Name ) )
        os.remove( os.path.join( PackageUtil.kInstallPath, "env_%s.csh" % self._Name ) )
        self.WriteEnvFile()
        commandText = """#!/bin/bash\nsource %s\ncd %s\ngit pull\n./configure\nsource env.sh\nscons -c\nscons""" % ( os.path.join( PackageUtil.kInstallPath, "env_%s.sh" % self._Name ), self.GetInstallPath() )
        self._InstallPipe += PackageUtil.ExecuteComplexCommand( commandText, True )
        return

class RAT4( RatReleases.RatReleasePost3 ):
    """ Temporary Rat release-4.00, install package."""
    def __init__( self ):
        """ Initiliase the rat 4.0 package."""
        super( RAT4, self ).__init__( "rat-4", "root-5.32.03", "scons-2.1.0", "geant4.9.5.p01", "clhep-2.1.1.0", "curl-7.26.0", "bzip2-1.0.6", \
                                          "avalanche-1", "zeromq-2.2.0", "xerces-c-3.1.1", "rat-4" )
        return

class RAT3( RatReleases.RatReleasePre4 ):
    """ Rat release-3.00, install package."""
    def __init__( self ):
        """ Initiliase the rat 3.0 package."""
        super( RAT3, self ).__init__( "rat-3", "root-5.32.03", "scons-2.1.0", "geant4.9.4.p01", "clhep-2.1.0.1", "curl-7.26.0", "bzip2-1.0.6", \
                                          "avalanche-1", "zeromq-2.2.0", "xerces-c-3.1.1", "release-3.00" )
        return

class RAT2( RatReleases.RatReleasePre3 ):
    """ Rat release-2.00, install package."""
    def __init__( self ):
        """ Initiliase the rat 2.0 package."""
        super( RAT2, self ).__init__( "rat-2", "root-5.28.00", "scons-2.1.0", "geant4.9.4.p01", "clhep-2.1.0.1", "curl-7.26.0", "bzip2-1.0.6", "release-2.00" )
        return

class RAT1( RatReleases.RatReleasePre2 ):
    """ Rat release-1.00, install package."""
    def __init__( self ):
        """ Initiliase the rat 1.0 package."""
        super( RAT1, self ).__init__( "rat-1", "root-5.24.00", "scons-1.2.0", "geant4.9.2.p02", "clhep-2.0.4.2", "release-1.00" )
        return

class RAT0( RatReleases.RatReleasePre2 ):
    """ Rat release-0.00, install package."""
    def __init__( self ):
        """ Initiliase the rat 0.0 package."""
        super( RAT0, self ).__init__( "rat-0", "root-5.24.00", "scons-1.2.0", "geant4.9.2.p02", "clhep-2.0.4.2", "release-0.00" )
        return

