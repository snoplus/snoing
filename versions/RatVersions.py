#!/usr/bin/env python
# Author P G Jones - 18/05/2012 <p.g.jones@qmul.ac.uk> : First revision
#        O Wasalski - 05/06/2012 <wasalski@berkeley.edu> : Added curl dependency to RAT-dev and rat-3
#        O Wasalski - 13/06/2012 <waslski@berkeley.edu> : Added bzip2 dependency to rat-dev
#        P G Jones - 21/06/2012 <p.g.jones@qmul.ac.uk> : New releases usage.
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
        self._GeantDependency = "geant4.9.4.p01"
        self._ClhepDependency = "clhep-2.1.0.1"
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
        return os.path.exists( os.path.join( self.GetInstallPath() ) )
    def _Download( self ):
        """ Git clone rat-dev."""
        self._DownloadPipe += PackageUtil.ExecuteSimpleCommand( "git", ["clone", "git@github.com:snoplus/rat.git",  self.GetInstallPath()], None, os.getcwd(), True ) # Force verbose
        return
    def _WriteEnvFile( self ):
        """ Write the environment file for rat."""
        self._EnvFile.AddGeant( self._DependencyPaths[self._GeantDependency], "env" )
        self._EnvFile.AppendLibraryPath( os.path.join( self._DependencyPaths[self._ClhepDependency], "lib" ) )
        self._EnvFile.AddEnvironment( "AVALANCHEROOT", self._DependencyPaths[self._AvalancheDependency] )
        self._EnvFile.AddEnvironment( "ZEROMQROOT", self._DependencyPaths[self._ZeromqDependency] )
        self._EnvFile.AddEnvironment( "XERCESCROOT", self._DependencyPaths[self._XercescDependency] )
        self._EnvFile.AppendLibraryPath( os.path.join( self._DependencyPaths[self._AvalancheDependency], "lib/cpp" ) )
        self._EnvFile.AppendLibraryPath( os.path.join( self._DependencyPaths[self._ZeromqDependency], "lib" ) )
        self._EnvFile.AppendLibraryPath( os.path.join( self._DependencyPaths[self._XercescDependency], "lib" ) )
        if self._DependencyPaths[self._CurlDependency] is not None: # Conditional Package, set to None if installed on system instead of locally
            self._EnvFile.AppendPath( os.path.join( self._DependencyPaths[self._CurlDependency], "bin" ) )
        if self._DependencyPaths[self._BzipDependency] is not None: # Conditional Package, set to None if installed on system instead of locally
            self._EnvFile.AddEnvironment( "BZIPROOT", self._DependencyPaths[self._BzipDependency] )
            self._EnvFile.AppendLibraryPath( os.path.join( self._DependencyPaths[self._BzipDependency], "lib" ) )
            # Must patch the rat config/EXTERNALS file.
            externalsFile = open( os.path.join( self.GetInstallPath(), "config/EXTERNAL.scons" ), "r" )
            text = externalsFile.read()
            externalsFile.close()
            externalsFile = open( os.path.join( self.GetInstallPath(), "config/EXTERNAL.scons" ), "w" )
            text.replace( "ext_deps['bz2']['path'] = None", "ext_deps['bz2']['path'] = os.environ['BZIPROOT']" )
            externalsFile.write( text )
            externalsFile.close()
        return

class RAT4( RatReleases.RatReleasePost3 ):
    """ Temporary Rat release-4.00, install package."""
    def __init__( self ):
        """ Initiliase the rat 4.0 package."""
        super( RAT4, self ).__init__( "rat-4", "root-5.32.03", "scons-2.1.0", "geant4.9.5.p01", "clhep-2.1.0.1", "curl-7.26.0", "bzip2-1.0.6", \
                                          "avalanche-1", "zeromq-2.2.0", "xerces-c-3.1.1", "ProposedPhysicsList" )
        return
    def _Download( self ):
        """ Derived classes should override this to download the package. Return True on success."""
        if self._Username is None:
            self._Username = raw_input( "Github username:" )
        if self._Password is None:
            print "Github password:"
            self._Password = getpass.getpass()
        self._DownloadPipe += PackageUtil.DownloadFile( "https://github.com/pgjones/rat/tarball/ProposedPhysicsList", self._Username, self._Password )
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

