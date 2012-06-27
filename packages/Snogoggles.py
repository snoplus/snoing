#!/usr/bin/env python
# Author P G Jones - 24/06/2012 <p.g.jones@qmul.ac.uk> : First revision
# The Snogoggles base class
import LocalPackage
import os
import PackageUtil

class Snogoggles( LocalPackage.LocalPackage ):
    """ Base snogoggles installer for snogoggles."""
    def __init__( self, name, sconsDependency, geant4Dependency, ratDependency, rootDependency, \
                      sfmlDependency, xercescDependency, avalancheDependency, zmqDependency ):
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
        return

    def GetDependencies( self ):
        """ Return the required dependencies."""
        return [self._SconsDependency, self._Geant4Dependency, self._RatDependency, self._RootDependency, \
                    self._SfmlDependency, self._XercescDependency, self._AvalancheDependency, self._ZeromqDependency]
    def _IsDownloaded( self ):
        """ Check if downloaded."""
        return os.path.exists( self.GetInstallPath() )
    def _IsInstalled( self ):
        """ Check if installed."""
        return os.path.exists( os.path.join( self.GetInstallPath(), "bin", "snogoggles" ) )
    def _Download( self ):
        """ Download snogoggles (git clone)."""
        self._DownloadPipe += PackageUtil.ExecuteSimpleCommand( "git", ["clone", "git@github.com:snoplus/snogoggles.git",  \
                                                                            self.GetInstallPath()], None, os.getcwd(), True ) # Force verbose 
        return
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
        self._InstallPipe += PackageUtil.ExecuteSimpleCommand( "./autoconfigure", [], env, self.GetInstallPath() )
        self._InstallPipe += PackageUtil.ExecuteComplexCommand( "cd %s\nsource env.sh\nscons" % self.GetInstallPath() )
        return
