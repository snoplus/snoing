#!/usr/bin/env python
#
# snoing
#
# Entry script decides what to do
#
# Author P G Jones - 12/05/2012 <p.g.jones@qmul.ac.uk> : First revision
# Author P G Jones - 23/06/2012 <p.g.jones@qmul.ac.uk> : Major refactor of snoing.
####################################################################################################
import optparse
import textlogger
import installmode
import exceptions
import system
import packagemanager

def print_error_message():
    """Print a standard error message if snoing fails."""
    print "Snoing has failed, please consult the above error messages or the snoing.log file."
    sys.exit(1)

if __name__ == "__main__":
    default_file_path = os.path.join(os.path.dirname(__file__), "settings.pkl")
    if os.path.isfile(default_file_path):
        default_file = open(default_file_path, "r")
        defaults = pickle.load(default_file)
        default_file.close()
    else: # No defaults to load, thus create
        defaults = {"cache_path" : "cache", "install_path", "install"}
    # First build the options and parse the calling command
    parser = optparse.OptionParser(usage = "usage: %prog [options] [package]", version="%prog 0.3")
    parser.add_option("-c", type="string", dest="cache_path", help="Cache path.", 
                      default=defaults["cache_path"])
    parser.add_option("-i", type="string", dest="install_path", help="Install path.", 
                      default=defaults["install_path"])
    parser.add_option("-v", action="store_true", dest="verbose", help="Verbose Install?", 
                      default=False)
    parser.add_option("-a", action="store_true", dest="all", help="All packages?")
    parser.add_option("-A", type="string", dest="arguments", help=optparse.SUPPRESS_HELP)

    installerGroup = optparse.OptionGroup(parser, "Optional Install modes", 
                                          ("Default snoing action is to install non graphically, i.e."
                                           " no viewer. This can be changed with the -g option."))
    installerGroup.add_option("-g", action="store_true", dest="graphical", help="Graphical install?", 
                              default=False)
    installerGroup.add_option("-x", action="store_true", dest="grid", help="Grid install (NO X11)?", 
                              default=False)
    parser.add_option_group(installerGroup)

    actionGroup = optparse.OptionGroup(parser, "Optional Actions", 
                                       ("Default snoing action is to install the specified package,"
                                        " which defaults to rat-dev."))
    actionGroup.add_option("-q", action="store_true", dest="query", help="Query Package Status?")
    actionGroup.add_option("-r", action="store_true", dest="remove", help="Remove the package?")
    actionGroup.add_option("-R", action="store_true", dest="forceRemove", help=optparse.SUPPRESS_HELP, 
                           default=False)
    actionGroup.add_option("-d", action="store_true", dest="dependency", help="Install dependencies only?")
    actionGroup.add_option("-p", action="store_true", dest="progress", help="Progress/update the package?")
    parser.add_option_group(actionGroup)

    githubGroup = optparse.OptionGroup(parser, "Github authentication Options", 
                                       "Supply a username or a github token, not both.")
    githubGroup.add_option("-u", type="string", dest="username", help="Github username")
    githubGroup.add_option("-t", type="string", dest="token", help="Github token")
    parser.add_option_group(githubGroup)
    (options, args) = parser.parse_args()
    # Dump the new defaults
    defaults["cache_path"] = options.cache_path
    defaults["install_path"] = options.install_path
    default_file = open(default_file_path, "w")
    pickle.dump(defaults, default_file)
    default_file.close()

    # Now create the logger, direct logging to snoing.log file
    logger = textlogger.TextLogger(os.path.join(os.path.dirname(__file__), "snoing.log"))
    # Now create the system
    if options.grid and options.graphical:
        !!!
    elif options.grid:
        install_mode = installmode.Grid
    elif options.graphical:
        install_mode = installmode.Graphical
    else:
        install_mode = installmode.Normal
    try:
        install_system = system.System(logger, options.cache_path, options.install_path, install_mode, options.arguments)
    except exceptions.SystemException, e:
        !!!
    # Now create the package manage and populate it
    package_manager = packagemanager.PackageManager(install_system, logger)
    package_manager.register_packages(os.path.join(os.path.dirname(__file__), "versions"))
    package_manager.authenticate(options.username, options.token)

    # Default action is to assume installing, check for other actions
    try:
        if options.all: # Wish to act on all packages
            if options.query: # Nothing todo, done automatically
                pass
            elif options.remove: # Wish to remove all packages
                shutil.rmtree(install_system.get_install_path())
            elif options.dependency: # Doesn't make sense
                Log.warn("Input options don't make sense.")
                PrintErrorMessage()
            elif options.progress: # Update all installed
                package_manager.update_all()
            else: # Wish to install all
                package_manager.install_all()
        else: # Only act on one package
            if options.grid == False: # Default local package
                package_name = "rat-dev"
            else: # Default grid package
                package_name = "rat-3"
            if len(args) != 0:
                package_name = args[0]
            if options.query: # Wish to query the package
                Log.Info( "Checking package %s install status" % package_name )
                if package_manager.CheckPackage( package_name ):
                    Log.Result( "Installed" )
                else:
                    Log.Warn( "Not Installed" )
            elif options.remove or options.forceRemove: # Wish to remove the package
                package_manager.RemovePackage( package_name, options.forceRemove )
            elif options.dependency: # Wish to install only the dependencies
                package_manager.InstallDependencies( package_name )
            elif options.progress: # Wish to update the package
                package_manager.UpdatePackage( package_name )
            else: # Wish to install the package
                package_manager.InstallPackage( package_name )
    except Exceptions.InstallException, e:
        print e
        PrintErrorMessage()
