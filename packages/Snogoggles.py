#!/usr/bin/env python
# Author P G Jones - 24/06/2012 <p.g.jones@qmul.ac.uk> : First revision
# Author P G Jones - 27/07/2012 <p.g.jones@qmul.ac.uk> : Added snogoggles versions.
# The Snogoggles base classes
import LocalPackage
import os
import PackageUtil

class Snogoggles( LocalPackage.LocalPackage ):
    """ Base snogoggles installer for snogoggles."""
    def __init__( self, name, sconsDependency, geant4Dependency, ratDependency, rootDependency, \
                      sfmlDependency, xercescDependency, avalancheDependency, zmqDependency, curlDependency, bzipDependency ):
        """ Initialise snogoggles."""
        super( Snogoggles, self ).__init__( name, True ) # Graphical only
        self._SconsDependency = sconsDependency
        self._Geant4Dependency = geant4Dependency
        self._RatDependency = ratDependency
        self._RootDependency = rootDependency
        self._SfmlDependency = sfmlDependency
        self._XercescDependency = xercescDependency
        self._AvalancheDependency = avalancheDependency
        self._ZeromqDependency = zmqDependency
        self._CurlDependency = curlDependency
        self._BzipDependency = bzipDependency
        return

    def GetDependencies( self ):
        """ Return the required dependencies."""
        return ["python", "python-dev", self._SconsDependency, self._Geant4Dependency, self._RatDependency, self._RootDependency, \
                    self._SfmlDependency, self._XercescDependency, self._AvalancheDependency, self._ZeromqDependency, \
                    self._CurlDependency, self._BzipDependency]
    def _IsInstalled( self ):
        """ Check if installed."""
        return os.path.exists( os.path.join( self.GetInstallPath(), "bin", "snogoggles" ) )
    def _Install( self ):
        """ Install Snogoggles."""
        env = os.environ
        env['RAT_SCONS'] = self._DependencyPaths[self._SconsDependency]
        env['GEANT4_BASE'] = self._DependencyPaths[self._Geant4Dependency]
        env['RATROOT'] = self._DependencyPaths[self._RatDependency]
        env['ROOTSYS'] = self._DependencyPaths[self._RootDependency]
        env['SFMLROOT'] = self._DependencyPaths[self._SfmlDependency]
        env['XERCESCROOT'] = self._DependencyPaths[self._XercescDependency]
        env['AVALANCHEROOT'] = self._DependencyPaths[self._AvalancheDependency]
        env['ZEROMQROOT'] = self._DependencyPaths[self._ZeromqDependency]
        if self._DependencyPaths[self._CurlDependency] is not None:
            env['PATH'] = os.path.join( self._DependencyPaths[self._CurlDependency], "bin" ) + ":" + env['PATH']
        if self._DependencyPaths[self._BzipDependency] is not None:
            env['BZIPROOT'] = self._DependencyPaths[self._BzipDependency]
        self._InstallPipe += PackageUtil.ExecuteSimpleCommand( "./autoconfigure", [], env, self.GetInstallPath() )
        self._InstallPipe += PackageUtil.ExecuteComplexCommand( "cd %s\nsource env.sh\nscons" % self.GetInstallPath() )
        return

class SnogogglesRelease( Snogoggles ):
    """ Release versions of snogoggles."""
    def __init__( self, name, tarName, sconsDependency, geant4Dependency, ratDependency, rootDependency, \
                      sfmlDependency, xercescDependency, avalancheDependency, zmqDependency, curlDependency, bzipDependency ):
        super( SnogogglesRelease, self ).__init__( name, sconsDependency, geant4Dependency, ratDependency, rootDependency, \
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
