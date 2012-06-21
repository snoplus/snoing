#!/usr/bin/env python
# Author P G Jones - 12/05/2012 <p.g.jones@qmul.ac.uk> : First revision
# SNO+ package manager
import PackageManager
import os
import inspect
import PackageUtil
import Rat
import pickle
import Log

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
        Log.kInfoFile = Log.LogFile( os.path.join( PackageUtil.kInstallPath, "README.md" ), True )
        Log.kInfoFile.Write( "## SNOING\nThis is a snoing install directory. Please alter only with snoing at %s" % __file__ )
        PackageUtil.kInstallPath = PackageUtil.kInstallPath
        # Set the local details file
        Log.kDetailsFile = Log.LogFile( os.path.join( os.path.dirname( __file__ ), "snoing.log" ) )
        # Now check for graphical option
        snoingSettingsPath = os.path.join( PackageUtil.kInstallPath, "snoing.pkl" )
        if os.path.exists( snoingSettingsPath ):
            settingsFile = open( snoingSettingsPath, "r" )
            if options.graphical != pickle.load( settingsFile ):
                raise Exception( "Install path chosen is marked as graphical = %s" % (not options.graphical ) )
            else:
                PackageUtil.kGraphical = options.graphical
            settingsFile.close()
        else:
            PackageUtil.kGraphical = options.graphical
            settingsFile = open( snoingSettingsPath, "w" )
            pickle.dump( options.graphical, settingsFile )
            settingsFile.close()
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
    parser.add_option( "-v", action="store_true", dest="verbose", help="Verbose Install?", default=False )
    parser.add_option( "-u", type="string", dest="username", help="Github username (for rat releases)" )
    parser.add_option( "-p", type="string", dest="password", help="Github password (for rat releases)" )
    (options, args) = parser.parse_args()
    Log.Header( "Registering Packages" )
    installer = snoing( options )
    PackageUtil.kVerbose = options.verbose
    if len(args) == 0:
        #Do something to all packages
        if options.query == True:
            Log.Header( "Checking all packages" )
            for packageName in installer.PackageNameGenerator():
                installer.CheckPackage( packageName )
        else:
            Log.Header( "Installing all packages" )
            for packageName in installer.PackageNameGenerator():
                installer.InstallPackage( packageName )
    else:
        if options.query == True:
            Log.Header( "Checking %s package" % args[0] )
            installer.CheckPackage( args[0] )
        else: 
            Log.Header( "Installing %s package" % args[0] )
            installer.InstallPackage( args[0] )
