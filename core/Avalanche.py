#!/usr/bin/env python
# Author P G Jones - 16/05/2012 <p.g.jones@qmul.ac.uk> : First revision
# The AVALANCHE packages base class
import LocalPackage
import os
import PackageUtil

class Avalanche( LocalPackage.LocalPackage ):
    """ Base avalanche installer for avalanche."""
    def __init__( self, name, tarName, zmqDependency, rootDependency ):
        """ Initialise avalanche with the tarName."""
        super( Avalanche, self ).__init__( name )
        self._TarName = tarName
        self._ZeromqDependency = zmqDependency
        self._RootDependency = rootDependency
        return
    def CheckState( self ):
        """ Check if downloaded and installed."""
        if os.path.exists( self.GetInstallPath() ):
            self._SetMode( 1 ) # Downloaded
        if os.path.exists( os.path.join( self.GetInstallPath(), "lib/cpp/libavalanche.so" ) ):
            self._SetMode( 2 ) # Installed as well
        return
    def GetDependencies( self ):
        """ Return the required dependencies."""
        return [self._ZeromqDependency, self._RootDependency]
    def _Download( self ):
        """ Derived classes should override this to download the package. Return True on success."""
        return PackageUtil.DownloadFile( "https://github.com/mastbaum/avalanche/tarball/" + self._TarName )
    def _Install( self ):
        """ Install the version."""
        PackageUtil.UnTarFile( self._TarName, self.GetInstallPath(), 1 )
        env = os.environ
        env['PATH'] = os.path.join( self._DependencyPaths['root-5.32.03'], "bin" ) + ":" + env['PATH']
        env['ROOTSYS'] = self._DependencyPaths['root-5.32.03']
        result = PackageUtil.ExecuteSimpleCommand( "make", ['CXXFLAGS=-L%s/lib -I%s/include' % (self._DependencyPaths["zeromq-2.2.0"], self._DependencyPaths["zeromq-2.2.0"]) ], env, os.path.join( self.GetInstallPath(), "lib/cpp" ) )
        return result
