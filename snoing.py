#!/usr/bin/env python
# Author P G Jones - 12/05/2012 <p.g.jones@qmul.ac.uk> : First revision
# SNO+ package manager
import PackageManager
import os
import inspect
import PackageUtil
import Rat
import Log
import Util
import sys

class snoing( PackageManager.PackageManager ):
    """ The package manager for sno+."""
    def __init__( self, options ):
        """ Initialise the snoing package manager."""
        import sys
        super( snoing, self ).__init__()
        Util.CheckSystem()
        PackageUtil.kCachePath = Util.BuildDirectory( options.cachePath )
        PackageUtil.kInstallPath = Util.BuildDirectory( options.installPath )
        Log.kInfoFile = Log.LogFile( os.path.join( PackageUtil.kInstallPath, "README.md" ), True )
        # Set the local details file
        Log.kDetailsFile = Log.LogFile( os.path.join( os.path.dirname( __file__ ), "snoing.log" ) )
        # Now check the graphical option is compatible with install directory
        snoingSettingsPath = os.path.join( PackageUtil.kInstallPath, "snoing.pkl" )
        graphical = Util.DeSerialise( snoingSettingsPath )
        if graphical is not None and graphical != options.graphical:
            Log.Error( "Install path chosen is marked as graphical = %s, please add or remove the '-g' option." % (not options.graphical ) )
            sys.exit(1)
        PackageUtil.kGraphical = options.graphical
        Util.Serialise( snoingSettingsPath, options.graphical )
        # First import all register all packages in the versions folder
        self.RegisterPackagesInDirectory( os.path.join( os.path.dirname( __file__ ), "versions" ) )
        # Now set the username or token for the rat packages
        for package in self._Packages:
            if isinstance( self._Packages[package], Rat.RatRelease ):
                self._Packages[package].SetGithubAuthentication( options.username, options.token )
    def PrintErrorMessage( self ):
        """Print a standard error message if snoing fails."""
        Log.Error( "Snoing has failed, please consult the above error messages or the snoing.log file." )
        sys.exit(1)

if __name__ == "__main__":
    import optparse
    # Load defaults from file
    defaultFilePath = os.path.join( os.path.dirname( __file__ ), "settings.pkl" )
    defaults = Util.DeSerialise( defaultFilePath )
    if defaults is None: # No defaults
        defaults = { "cache" : "cache", "install" : "install" }
    parser = optparse.OptionParser( usage = "usage: %prog [options] [package]", version="%prog 0.2" )
    parser.add_option( "-c", type="string", dest="cachePath", help="Cache path.", default=defaults["cache"] )
    parser.add_option( "-i", type="string", dest="installPath", help="Install path.", default=defaults["install"] )
    parser.add_option( "-g", action="store_true", dest="graphical", help="Graphical install?" )
    parser.add_option( "-q", action="store_true", dest="query", help="Query Package Status?" )
    parser.add_option( "-r", action="store_true", dest="remove", help="Remove the package instead?" )
    parser.add_option( "-d", action="store_true", dest="dependency", help="Dependencies only?" )
    parser.add_option( "-v", action="store_true", dest="verbose", help="Verbose Install?", default=False )
    parserGroup = optparse.OptionGroup( parser, "Github authentication Options", "Supply a username or a github token, not both." )
    parserGroup.add_option( "-u", type="string", dest="username", help="Github username" )
    parserGroup.add_option( "-t", type="string", dest="token", help="Github token" )
    parser.add_option_group( parserGroup )
    (options, args) = parser.parse_args()
    # Save the defaults to file
    defaults["cache"] = options.cachePath
    defaults["install"] = options.installPath
    Util.Serialise( defaultFilePath, defaults )
    # Construct snoing installer
    Log.Header( "Registering Packages" )
    PackageUtil.kVerbose = options.verbose
    installer = snoing( options )
    if len(args) == 0:
        #Do something to all packages
        if options.query == True:
            Log.Header( "Checking all packages" )
            for packageName in installer.PackageNameGenerator():
                installer.CheckPackage( packageName )
        else:
            Log.Header( "Installing all packages" )
            for packageName in installer.PackageNameGenerator():
                try:
                    installer.InstallPackage( packageName )
                except:
                    installer.PrintErrorMessage()
    else:
        if options.query == True:
            Log.Header( "Checking %s package" % args[0] )
            installer.CheckPackage( args[0] )
        elif options.dependency == True:
            Log.Header( "Installing %s package dependencies" % args[0] )
            try:
                installer.InstallPackageDependencies( args[0] )
            except:
                installer.PrintErrorMessage()
        elif options.remove == True:
            Log.Header( "Removing %s package" % args[0] )
            try:
                installer.RemovePackage( args[0] )
            except:
                installer.PrintErrorMessage()
        else: 
            Log.Header( "Installing %s package" % args[0] )
            try:
                installer.InstallPackage( args[0] )
            except:
                installer.PrintErrorMessage()
