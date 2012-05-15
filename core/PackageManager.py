#!/usr/bin/env python
# Author P G Jones - 12/05/2012 <p.g.jones@qmul.ac.uk> : First revision
# Base class package manager
import CommandPackage
import LocalPackage

class PackageManager( object ):
    """ Manages a dictionary of packages that the software can install."""
    def __init__( self ):
        """ Initialise the package manager."""
        self._Packages = {}
        return
    def RegisterPackage( self, package ):
        """ Add the package to the list of known packages."""
        print "Registering package %s" % package.GetName()
        self._Packages[package.GetName()] = package
        return
    def InstallPackage( self, packageName ):
        """ Install the package by package name."""
        if not packageName in self._Packages.keys():
            print "Package: %s not found" % packageName
        # First check if the package is already installed
        package = self._Packages[packageName]
        package.CheckState()
        if package.IsInstalled():
            # Great
            return
        if isinstance( package, CommandPackage.CommandPackage ):
            # Ah user must install this system wide...
            raise Exception( "Package %s must be installed manually." % package.GetName() )
        # Not installed and a LocalPackage, thus can install. Start with dependencies, and build dependency dict
        dependencyPaths = {}
        for dependency in package.GetDependencies(): 
            self.InstallPackage( dependency )
            dependencyPaths[dependency] = self._Packages[dependency].GetInstallPath()
        # Now we can install this package
        package.SetDependencyPaths( dependencyPaths )
        package.Install()
        print "Package: %s installed." % package.GetName()
        return
