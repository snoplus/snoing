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
import Exceptions

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
        Log.Header( "Caching to %s, installing to %s" % ( PackageUtil.kCachePath, PackageUtil.kInstallPath ) )
        # Now check the install options are compatible with install directory
        if options.graphical == True and options.grid == True:
            Log.Error( "Cannot be both graphical and grid." )
            self.PrintErrorMessage()
        snoingSettingsPath = os.path.join( PackageUtil.kInstallPath, "snoing.pkl" )
        installModes = Util.DeSerialise( snoingSettingsPath )
        # Set the file options if not set
        if installModes is None: 
            installModes = { "Graphical" : options.graphical, "Grid" : options.grid }
            Util.Serialise( snoingSettingsPath, installModes )
        # Check the options match
        if installModes["Graphical"] != options.graphical or installModes["Grid"] != options.grid:
            Log.Error( "Install mode for install directory does not match that specified. Install path is graphical %s and grid %s" \
                           % ( options.graphical, options.grid ) )
            self.PrintErrorMessage()
        PackageUtil.kGraphical = options.graphical
        PackageUtil.kGrid = options.grid
        # First import all register all packages in the versions folder
        self.RegisterPackagesInDirectory( os.path.join( os.path.dirname( __file__ ), "versions" ) )
        return
    def Authenticate( self, options ):
        """ Set the github authentication."""
        # Now set the username or token for the rat packages
        for package in self._Packages:
            if isinstance( self._Packages[package], Rat.RatRelease ):
                self._Packages[package].SetGithubAuthentication( options.username, options.token )
    def PrintErrorMessage( self ):
        """Print a standard error message if snoing fails."""
        Log.Error( "Snoing has failed, please consult the above error messages or the snoing.log file." )
        sys.exit(1)
        return

if __name__ == "__main__":
    import optparse
    # Load defaults from file
    defaultFilePath = os.path.join( os.path.dirname( __file__ ), "settings.pkl" )
    defaults = Util.DeSerialise( defaultFilePath )
    if defaults is None: # No defaults
        defaults = { "cache" : "cache", "install" : "install" }
    parser = optparse.OptionParser( usage = "usage: %prog [options] [package]", version="%prog 0.3" )
    parser.add_option( "-c", type="string", dest="cachePath", help="Cache path.", default=defaults["cache"] )
    parser.add_option( "-i", type="string", dest="installPath", help="Install path.", default=defaults["install"] )
    parser.add_option( "-v", action="store_true", dest="verbose", help="Verbose Install?", default=False )
    parser.add_option( "-a", action="store_true", dest="all", help="All packages?" )

    installerGroup = optparse.OptionGroup( parser, "Optional Install modes", "Default snoing action is to install non graphically, i.e. no viewer. This can be changed with the -g option. If installing on the grid use the -x option." )
    installerGroup.add_option( "-g", action="store_true", dest="graphical", help="Graphical install?", default=False )
    installerGroup.add_option( "-x", action="store_true", dest="grid", help="Grid install (NO X11)?", default=False )
    parser.add_option_group( installerGroup )

    actionGroup = optparse.OptionGroup( parser, "Optional Actions", "Default snoing action is to install the specified package, which defaults to rat-dev." )
    actionGroup.add_option( "-q", action="store_true", dest="query", help="Query Package Status?" )
    actionGroup.add_option( "-r", action="store_true", dest="remove", help="Remove the package?" )
    actionGroup.add_option( "-R", action="store_true", dest="forceRemove", help=optparse.SUPPRESS_HELP, default=False )
    actionGroup.add_option( "-d", action="store_true", dest="dependency", help="Install dependencies only?" )
    parser.add_option_group( actionGroup )

    githubGroup = optparse.OptionGroup( parser, "Github authentication Options", "Supply a username or a github token, not both." )
    githubGroup.add_option( "-u", type="string", dest="username", help="Github username" )
    githubGroup.add_option( "-t", type="string", dest="token", help="Github token" )
    parser.add_option_group( githubGroup )
    (options, args) = parser.parse_args()
    # Save the defaults to file
    defaults["cache"] = options.cachePath
    defaults["install"] = options.installPath
    Util.Serialise( defaultFilePath, defaults )
    # Construct snoing installer
    Log.Header( "Registering Packages" )
    PackageUtil.kVerbose = options.verbose
    installer = snoing( options )
    installer.Authenticate( options )

    # Default action is to assume installing, check for other actions
    try:
        if options.all: # Wish to act on all packages
            if options.query: # Wish to query all packages
                installer.CheckAll()
            elif options.remove: # Wish to remove all packages
                shutil.rmtree( PackageUtil.kInstallPath )
            elif options.dependency: # Doesn't make sense
                Log.warn( "Input options don't make sense." )
                installer.PrintErrorMessage()
            else: # Wish to install all
                installer.InstallAll()
        else: # Only act on one package
            if options.grid == False: # Default local package
                packageName = "rat-dev"
            else: # Default grid package
                packageName = "rat-3"
            if len(args) != 0:
                packageName = args[0]
            if options.query: # Wish to query the package
                Log.Info( "Checking package %s install status" % packageName )
                if installer.CheckPackage( packageName ):
                    Log.Result( "Installed" )
                else:
                    Log.Warn( "Not Installed" )
            elif options.remove or options.forceRemove: # Wish to remove the package
                installer.RemovePackage( packageName, options.forceRemove )
            elif options.dependency: # Wish to install only the dependencies
                installer.InstallDependencies( packageName )
            else: # Wish to install the package
                installer.InstallPackage( packageName )
    except Exceptions.InstallException, e:
        print e
        installer.PrintErrorMessage()
