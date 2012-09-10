#!/usr/bin/env python
# Author P G Jones - 21/06/2012 <p.g.jones@qmul.ac.uk> : First revision
# Base classes for the various rat releases, oldest at the bottom
# RAT-2 is first curl and bzip one!
# RAT-3 adds avalanche, xerces and zeromq extra
# RAT-4 slightly changes the geant dependency
import os
import Rat
import PackageUtil

class RatReleasePost3( Rat.RatRelease ):
    """ Base package installer for rat release 3."""
    def __init__( self, name,  rootDependency, sconsDependency, geantDependency, clhepDependency, curlDependency, bzipDependency, \
                  avalancheDependency, zeromqDependency, xercescDependency, tarName ):
        """ Initlaise, take extra dependencies."""
        super( RatReleasePost3, self ).__init__( name,  rootDependency, sconsDependency, tarName )
        self._GeantDependency = geantDependency
        self._ClhepDependency = clhepDependency
        self._CurlDependency = curlDependency
        self._BzipDependency = bzipDependency
        self._AvalancheDependency = avalancheDependency
        self._ZeromqDependency = zeromqDependency
        self._XercescDependency = xercescDependency
        return

    def _GetDependencies( self ):
        """ Return the extra dependencies."""
        return [ self._GeantDependency, self._ClhepDependency, self._CurlDependency, self._BzipDependency, self._AvalancheDependency, \
                 self._ZeromqDependency, self._XercescDependency ]
    def _WriteEnvFile( self ):
        """ Diff geant env file and no need to patch rat."""
        self._EnvFile.AddSource( self._DependencyPaths[self._GeantDependency], "bin/geant4" )
        self._EnvFile.AppendLibraryPath( os.path.join( self._DependencyPaths[self._ClhepDependency], "lib" ) )
        self._EnvFile.AddEnvironment( "AVALANCHEROOT", self._DependencyPaths[self._AvalancheDependency] )
        if self._DependencyPaths[self._ZeromqDependency] is not None: # Conditional Package, set to None if installed on system instead of locally
            self._EnvFile.AddEnvironment( "ZEROMQROOT", self._DependencyPaths[self._ZeromqDependency] )
            self._EnvFile.AppendLibraryPath( os.path.join( self._DependencyPaths[self._ZeromqDependency], "lib" ) )
        if self._DependencyPaths[self._XercescDependency] is not None: # Conditional Package, set to None if installed on system instead of locally
            self._EnvFile.AddEnvironment( "XERCESCROOT", self._DependencyPaths[self._XercescDependency] )
            self._EnvFile.AppendLibraryPath( os.path.join( self._DependencyPaths[self._XercescDependency], "lib" ) )
        self._EnvFile.AppendPath( os.path.join( self._DependencyPaths[self._GeantDependency], "bin" ) )
        self._EnvFile.AppendPath( os.path.join( self._DependencyPaths[self._ClhepDependency], "bin" ) )
        self._EnvFile.AppendLibraryPath( os.path.join( self._DependencyPaths[self._ClhepDependency], "lib" ) )
        self._EnvFile.AppendLibraryPath( os.path.join( self._DependencyPaths[self._AvalancheDependency], "lib/cpp" ) )
        if self._DependencyPaths[self._CurlDependency] is not None: # Conditional Package, set to None if installed on system instead of locally
            self._EnvFile.AppendPath( os.path.join( self._DependencyPaths[self._CurlDependency], "bin" ) )
        if self._DependencyPaths[self._BzipDependency] is not None: # Conditional Package, set to None if installed on system instead of locally
            self._EnvFile.AddEnvironment( "BZIPROOT", self._DependencyPaths[self._BzipDependency] )
            self._EnvFile.AppendLibraryPath( os.path.join( self._DependencyPaths[self._BzipDependency], "lib" ) )
        return

class RatReleasePre4( Rat.RatRelease ):
    """ Base package installer for rat release 3."""
    def __init__( self, name,  rootDependency, sconsDependency, geantDependency, clhepDependency, curlDependency, bzipDependency, \
                      avalancheDependency, zeromqDependency, xercescDependency, tarName ):
        """ Initlaise, take extra dependencies."""
        super( RatReleasePre4, self ).__init__( name,  rootDependency, sconsDependency, tarName )
        self._GeantDependency = geantDependency
        self._ClhepDependency = clhepDependency
        self._CurlDependency = curlDependency
        self._BzipDependency = bzipDependency
        self._AvalancheDependency = avalancheDependency
        self._ZeromqDependency = zeromqDependency
        self._XercescDependency = xercescDependency
        return

    def _GetDependencies( self ):
        """ Return the extra dependencies."""
        return [ self._GeantDependency, self._ClhepDependency, self._CurlDependency, self._BzipDependency, self._AvalancheDependency, \
                     self._ZeromqDependency, self._XercescDependency ]
    def _WriteEnvFile( self ):
        """ Add the extra info to the env file."""
        self._EnvFile.AddSource( self._DependencyPaths[self._GeantDependency], "env" )
        self._EnvFile.AppendLibraryPath( os.path.join( self._DependencyPaths[self._ClhepDependency], "lib" ) )
        self._EnvFile.AddEnvironment( "AVALANCHEROOT", self._DependencyPaths[self._AvalancheDependency] )
        if self._DependencyPaths[self._ZeromqDependency] is not None: # Conditional Package, set to None if installed on system instead of locally
            self._EnvFile.AddEnvironment( "ZEROMQROOT", self._DependencyPaths[self._ZeromqDependency] )
            self._EnvFile.AppendLibraryPath( os.path.join( self._DependencyPaths[self._ZeromqDependency], "lib" ) )
        if self._DependencyPaths[self._XercescDependency] is not None: # Conditional Package, set to None if installed on system instead of locally
            self._EnvFile.AddEnvironment( "XERCESCROOT", self._DependencyPaths[self._XercescDependency] )
            self._EnvFile.AppendLibraryPath( os.path.join( self._DependencyPaths[self._XercescDependency], "lib" ) )
        self._EnvFile.AppendLibraryPath( os.path.join( self._DependencyPaths[self._AvalancheDependency], "lib/cpp" ) )
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
            text = text.replace( "ext_deps['bz2']['path'] = None", "ext_deps['bz2']['path'] = os.environ['BZIPROOT']" )
            externalsFile.write( text )
            externalsFile.close()
        return

class RatReleasePre3( Rat.RatRelease ):
    """ Base package installer for rat release 2."""
    def __init__( self, name,  rootDependency, sconsDependency, geantDependency, clhepDependency, curlDependency, bzipDependency, tarName ):
        """ Initlaise, take extra dependencies."""
        super( RatReleasePre3, self ).__init__( name,  rootDependency, sconsDependency, tarName )
        self._GeantDependency = geantDependency
        self._ClhepDependency = clhepDependency
        self._CurlDependency = curlDependency
        self._BzipDependency = bzipDependency
        return

    def _GetDependencies( self ):
        """ Return the extra dependencies."""
        return [ self._GeantDependency, self._ClhepDependency, self._CurlDependency, self._BzipDependency ]
    def _WriteEnvFile( self ):
        """ Add the extra info to the env file."""
        self._EnvFile.AddSource( self._DependencyPaths[self._GeantDependency], "env" )
        self._EnvFile.AppendLibraryPath( os.path.join( self._DependencyPaths[self._ClhepDependency], "lib" ) )
        if self._DependencyPaths[self._CurlDependency] is not None: # Conditional Package, set to None if installed on system instead of locally
            self._EnvFile.AppendPath( os.path.join( self._DependencyPaths[self._CurlDependency], "bin" ) )
        if self._DependencyPaths[self._BzipDependency] is not None: # Conditional Package, set to None if installed on system instead of locally
            self._EnvFile.AddEnvironment( "BZIPROOT", self._DependencyPaths[self._BzipDependency] )
            self._EnvFile.AppendLibraryPath( os.path.join( self._DependencyPaths[self._BzipDependency], "lib" ) )
            # Must patch the rat config/EXTERNALS file.
            externalsFile = open( os.path.join( self.GetInstallPath(), "config/EXTERNAL.scons" ), "r" )
            text = externalsFile.read()
            exterbalsFile.close()
            externalsFile = open( os.path.join( self.GetInstallPath(), "config/EXTERNAL.scons" ), "w" )
            text = text.replace( "ext_deps['bz2']['path'] = None", "ext_deps['bz2']['path'] = os.environ['BZIPROOT']" )
            externalsFile.write( text )
            externalsFile.close()
        return

class RatReleasePre2( Rat.RatRelease ):
    """ Base package installer for rat releases 0, 1."""
    def __init__( self, name,  rootDependency, sconsDependency, geantDependency, clhepDependency, tarName ):
        """ Initlaise, take extra dependencies."""
        super( RatReleasePre2, self ).__init__( name,  rootDependency, sconsDependency, tarName )
        self._GeantDependency = geantDependency
        self._ClhepDependency = clhepDependency
        return

    def _GetDependencies( self ):
        """ Return the extra dependencies."""
        return [ self._GeantDependency, self._ClhepDependency ]
    def _WriteEnvFile( self ):
        """ Add the extra info to the env file."""
        self._EnvFile.AddSource( self._DependencyPaths[self._GeantDependency], "env" )
        self._EnvFile.AppendLibraryPath( os.path.join( self._DependencyPaths[self._ClhepDependency], "lib" ) )
        return
