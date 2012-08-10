#!/usr/bin/env python
# Author P G Jones - 24/06/2012 <p.g.jones@qmul.ac.uk> : First revision
# Author P G Jones - 27/07/2012 <p.g.jones@qmul.ac.uk> : Added snogoggles versions.
# Author P G Jones - 27/07/2012 <p.g.jones@qmul.ac.uk> : Moved to env file builder.
# The Snogoggles base classes
import LocalPackage
import os
import PackageUtil
import EnvFileBuilder

class Snogoggles( LocalPackage.LocalPackage ):
    """ Base snogoggles installer for snogoggles."""
    def __init__( self, name, sconsDependency, geant4Dependency, clhepDependency, ratDependency, rootDependency, \
                      sfmlDependency, xercescDependency, avalancheDependency, zmqDependency, curlDependency, bzipDependency ):
        """ Initialise snogoggles."""
        super( Snogoggles, self ).__init__( name, True ) # Graphical only
        self._SconsDependency = sconsDependency
        self._Geant4Dependency = geant4Dependency
        self._ClhepDependency = clhepDependency
        self._RatDependency = ratDependency
        self._RootDependency = rootDependency
        self._SfmlDependency = sfmlDependency
        self._XercescDependency = xercescDependency
        self._AvalancheDependency = avalancheDependency
        self._ZeromqDependency = zmqDependency
        self._CurlDependency = curlDependency
        self._BzipDependency = bzipDependency
        self._EnvFile = EnvFileBuilder.EnvFileBuilder( "#snogoggles environment\n" )
        return

    def GetDependencies( self ):
        """ Return the required dependencies."""
        dependencies = ["python", "python-dev", self._SconsDependency, self._Geant4Dependency, self._ClhepDependency, self._RatDependency, \
                            self._RootDependency, self._SfmlDependency, self._XercescDependency, self._AvalancheDependency, \
                            self._ZeromqDependency, self._CurlDependency, self._BzipDependency]
        return dependencies
    def _IsInstalled( self ):
        """ Check if installed."""
        return os.path.exists( os.path.join( self.GetInstallPath(), "bin", "snogoggles" ) )
    def _Install( self ):
        """ Install Snogoggles."""
        self.WriteEnvFile()
        self._InstallPipe += PackageUtil.ExecuteComplexCommand( "source env_%s.sh\ncd %s\nscons" % (self._Name, self.GetInstallPath() ) )
        return
    def WriteEnvFile( self ):
        """ Adds general parts and then writes the env file."""
        self._EnvFile.AddEnvironment( "VIEWERROOT", self.GetInstallPath() )
        self._EnvFile.AddEnvironment( "ROOTSYS", self._DependencyPaths[self._RootDependency] )
        self._EnvFile.AddEnvironment( "SFMLROOT", self._DependencyPaths[self._SfmlDependency] )
        self._EnvFile.AddEnvironment( "GLEWROOT", os.path.join( self._DependencyPaths[self._SfmlDependency], "extlibs" ) )
        self._EnvFile.AddEnvironment( "XERCESCROOT", self._DependencyPaths[self._XercescDependency] )
        self._EnvFile.AddEnvironment( "AVALANCHEROOT", self._DependencyPaths[self._AvalancheDependency] )
        self._EnvFile.AddEnvironment( "ZEROMQROOT", self._DependencyPaths[self._ZeromqDependency] )
        if self._DependencyPaths[self._BzipDependency] is not None:
            self._EnvFile.AddEnvironment( "BZIPROOT", self._DependencyPaths[self._BzipDependency] )

        if self._DependencyPaths[self._CurlDependency] is not None:
            self._EnvFile.AppendPath( os.path.join( self._DependencyPaths[self._CurlDependency], "bin" ) )
        self._EnvFile.AppendPath( os.path.join( self.GetInstallPath(), "bin" ) )
        self._EnvFile.AppendPath( os.path.join( self._DependencyPaths[self._RootDependency], "bin" ) )
        self._EnvFile.AppendPath( os.path.join( self._DependencyPaths[self._ClhepDependency], "bin" ) )
        self._EnvFile.AppendPath( os.path.join( self._DependencyPaths[self._SconsDependency], "script" ) )

        self._EnvFile.AppendPythonPath( os.path.join( self.GetInstallPath(), "python" ) )

        # Library path is always after the environment exports/setenvs
        self._EnvFile.AppendLibraryPath( os.path.join( self._DependencyPaths[self._ClhepDependency], "lib" ) )
        self._EnvFile.AppendLibraryPath( "$ROOTSYS/lib:$AVALANCHEROOT/lib/cpp:$ZEROMQROOT/lib:$SFMLROOT/lib:$XERCESCROOT/lib:$GLEWROOT/lib" )
        self._WriteEnvFile()
        self._EnvFile.WriteEnvFiles( PackageUtil.kInstallPath, "env_%s" % self._Name )
        return
    # Functions that must be implemented by sub classes
    def _WriteEnvFile( self ):
        """ Sub classes should add parts to the env file."""
        pass

class SnogogglesRelease( Snogoggles ):
    """ Release versions of snogoggles."""
    def __init__( self, name, tarName, sconsDependency, geant4Dependency, clhepDependency, ratDependency, rootDependency, \
                      sfmlDependency, xercescDependency, avalancheDependency, zmqDependency, curlDependency, bzipDependency ):
        super( SnogogglesRelease, self ).__init__( name, sconsDependency, geant4Dependency, clhepDependency, ratDependency, rootDependency, \
                                                       sfmlDependency, xercescDependency, avalancheDependency, zmqDependency, \
                                                       curlDependency, bzipDependency )
        self._TarName = tarName
        return
    def _IsDownloaded( self ):
        """ Check if tarball has been downloaded."""
        return os.path.exists( os.path.join( PackageUtil.kCachePath, self._TarName ) )
    def _Download( self ):
        """ Derived classes should override this to download the package. Return True on success."""
        self._DownloadPipe += PackageUtil.DownloadFile( "https://github.com/snoplus/snogoggles/tarball/" + self._TarName )
        return
    def _Install( self ):
        """ Untar the file first."""
        self._InstallPipe += PackageUtil.UnTarFile( self._TarName, self.GetInstallPath(), 1 )
        super( SnogogglesRelease, self )._Install()
        return
    def _WriteEnvFile( self ):
        """ Previous releases had a special geant4 environment."""
        self._EnvFile.AddSource( self._DependencyPaths[self._Geant4Dependency], "env" )
        self._EnvFile.AddEnvironment( "RATROOT", self._DependencyPaths[self._RatDependency] )
        self._EnvFile.AppendLibraryPath( "$G4LIB/$G4SYSTEM" )
        self._EnvFile.AppendPythonPath( os.path.join( self._DependencyPaths[self._SconsDependency], "engine" ) )
        self._EnvFile.AppendLibraryPath( "$RATROOT/lib" )
        return
