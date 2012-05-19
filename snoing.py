#!/usr/bin/env python
# Author P G Jones - 12/05/2012 <p.g.jones@qmul.ac.uk> : First revision
# SNO+ package manager
import PackageManager
import os
import inspect
import PackageUtil
import LocalPackage
import CommandPackage
import Rat
import getpass

class snoing( PackageManager.PackageManager ):
    """ The package manager for sno+."""
    def __init__( self, options ):
        """ Initialise the snoing package manager."""
        super( snoing, self ).__init__()
        if options.cachePath[0] == '/': # Global path
            self._CachePath = options.cachePath
        else:
            self._CachePath = os.path.join( os.getcwd(), options.cachePath )
        if not os.path.exists( self._CachePath ):
            os.makedirs( self._CachePath )
        if len( options.installPath ) != 0 and options.installPath[0] == '/': # Global path
            self._InstallPath = options.installPath
        else:
            self._InstallPath = os.path.join( os.getcwd(), options.installPath )
        if not os.path.exists( self._InstallPath ):
            os.makedirs( self._InstallPath )
        PackageUtil.kCachePath = self._CachePath
        PackageUtil.kInstallPath = self._InstallPath
        # Now check for graphical option
        graphical = False
        if options.graphical != None:
            graphical = options.graphical
        # First import all register all packages in this folder
        for module in os.listdir( os.path.join( os.path.dirname( __file__ ), "packages" ) ):
            if module == 'snoing.py' or module[-3:] != '.py':
                continue
            packageSet = __import__( module[:-3], locals(), globals() )
            for name, obj in inspect.getmembers( packageSet ):
                if inspect.isclass( obj ): 
                    if issubclass( obj, LocalPackage.LocalPackage ):
                        currentPackage = obj( self._CachePath, options.installPath, graphical )
                        self.RegisterPackage( currentPackage )
                        if issubclass( obj, Rat.RatReleasePre3 ):
                            password = options.password
                            if options.password == None:
                                password = getpass.getpass()
                            currentPackage.SetUsernamePassword( options.username, password )
                    elif issubclass( obj, CommandPackage.CommandPackage ):
                        self.RegisterPackage( obj() )

if __name__ == "__main__":
    import optparse
    parser = optparse.OptionParser( usage = "usage: %prog [options] [package]", version="%prog 1.0" )
    parser.add_option( "-c", type="string", dest="cachePath", help="Cache path.", default="cache" )
    parser.add_option( "-i", type="string", dest="installPath", help="Install path.", default="" )
    parser.add_option( "-g", action="store_true", dest="graphical", help="Graphical install?" )
    parser.add_option( "-u", type="string", dest="username", help="Github username (for rat releases)" )
    parser.add_option( "-p", type="string", dest="password", help="Github password (for rat releases)" )
    (options, args) = parser.parse_args()
    installer = snoing( options )
    if len(args) == 0:
        #Install all
        print "Installing all"
    else:
        installer.InstallPackage( args[0] )
