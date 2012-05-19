#!/usr/bin/env python
# Author P G Jones - 19/05/2012 <p.g.jones@qmul.ac.uk> : First revision
# The Avalanche package
import LocalPackage
import PackageUtil

class Avalanche( LocalPackage.LocalPackage ):
    """ Avalanche install package."""
    def __init__( self, cachePath, installPath ):
        """ Initlaise the ZMQ packages."""
        super( Avalanche, self ).__init__( "avalanche", cachePath, installPath, False )
        return
    def CheckState( self ):
        """ Check if downloaded and installed."""
        if os.path.exists( self.GetInstallPath() ):
            self._SetMode( 1 ) # Downloaded
        if os.path.exists( os.path.join( self.GetInstallPath(), "lib/cpp/libavalanche.so" ) ):
            self._SetMode( 2 ) # Installed as well
        return
    def GetDependencies( self ):
        """ Return the avalanche dependencies."""
        return ["zeromq-2.2.0", "root-5.32.03"]
    def _Download( self ):
        """ Download the ? version."""
        result = PackageUtil.ExecuteSimpleCommand( "git", ["clone", "git://github.com/mastbaum/avalanche.git", self.GetInstallPath()] )
        return result && PackageUtil.ExecuteSimpleCommand( "make", ["clean"], None, self.GetInstallPath() )
    def _Install( self ):
        """ Install the ? version."""
        env = os.environ
        env['PATH'] = self._DependencyPaths['root-5.32.03'] + ":" + env['PATH']
        result = PackageUtil.ExecuteSimpleCommand( "make", ['CXXFLAGS=-L%s/lib -I%s/include'], env, os.path.join( self.GetInstallPath(), "lib/cpp" ) )
        return result
