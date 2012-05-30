#!/usr/bin/env python
# Author P G Jones - 12/05/2012 <p.g.jones@qmul.ac.uk> : First revision
# SNO+ package manager
import PackageManager
import os
import inspect
import PackageUtil
import Rat
import pickle

class snoing( PackageManager.PackageManager ):
    """ The package manager for sno+."""
    def __init__( self, options ):
        """ Initialise the snoing package manager."""
        super( snoing, self ).__init__()
        if options.cachePath[0] == '/': # Global path
            PackageUtil.kCachePath = options.cachePath
        else:
            PackageUtil.kCachePath = os.path.join( os.getcwd(), options.cachePath )
        if not os.path.exists( PackageUtil.kCachePath ):
            os.makedirs( PackageUtil.kCachePath )
        if options.installPath[0] == '/': # Global path
            PackageUtil.kInstallPath = options.installPath
        else:
            PackageUtil.kInstallPath = os.path.join( os.getcwd(), options.installPath )
        if not os.path.exists( PackageUtil.kInstallPath ):
            os.makedirs( PackageUtil.kInstallPath )
            with open( os.path.join( PackageUtil.kInstallPath, "README.md" ), "w" ) as infoFile:
                infoFile.write( "## SNOING\nThis is a snoing install directory. Please alter only with snoing at %s" % __file__ )
        PackageUtil.kInstallPath = PackageUtil.kInstallPath
        # Now check for graphical option
        snoingSettingsPath = os.path.join( PackageUtil.kInstallPath, "snoing.pkl" )
        if os.path.exists( snoingSettingsPath ):
            with open( snoingSettingsPath, "r" ) as settingsFile:
                if options.graphical != pickle.load( settingsFile ):
                    raise Exception( "Install path chosen is marked as graphical = %s" % (not options.graphical ) )
                else:
                    PackageUtil.kGraphical = options.graphical
        else:
            PackageUtil.kGraphical = options.graphical
            with open( snoingSettingsPath, "w" ) as settingsFile:
                pickle.dump( options.graphical, settingsFile )
        # First import all register all packages in this folder
        self.RegisterPackagesInDirectory( os.path.join( os.path.dirname( __file__ ), "packages" ) )
        # Now set the username password for the rat packages
        for package in self._Packages:
            if isinstance( self._Packages[package], Rat.RatRelease ):
                self._Packages[package].SetUsernamePassword( options.username, options.password )
        

if __name__ == "__main__":
    import optparse
    parser = optparse.OptionParser( usage = "usage: %prog [options] [package]", version="%prog 1.0" )
    parser.add_option( "-c", type="string", dest="cachePath", help="Cache path.", default="cache" )
    parser.add_option( "-i", type="string", dest="installPath", help="Install path.", default="install" )
    parser.add_option( "-g", action="store_true", dest="graphical", help="Graphical install?" )
    parser.add_option( "-q", action="store_true", dest="query", help="Query Package Status?" )
    parser.add_option( "-u", type="string", dest="username", help="Github username (for rat releases)" )
    parser.add_option( "-p", type="string", dest="password", help="Github password (for rat releases)" )
    (options, args) = parser.parse_args()
    installer = snoing( options )
    if len(args) == 0:
        #Install all
        print "Installing all"
    else:
        if options.query == True:
            print args[0], installer.CheckPackage( args[0] )
        else:
            installer.InstallPackage( args[0] )
