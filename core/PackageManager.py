#!/usr/bin/env python
# Author P G Jones - 12/05/2012 <p.g.jones@qmul.ac.uk> : First revision
# Base class package manager
import CommandPackage
import ConditionalPackage
import LocalPackage
import os
import inspect

class PackageManager( object ):
    """ Manages a dictionary of packages that the software can install."""
    def __init__( self ):
        """ Initialise the package manager."""
        self._Packages = {}
        return
    def RegisterPackagesInDirectory( self, folderPath ):
        """ Register all the packages in the folderPath. """
        for module in os.listdir( folderPath ):
            if module[-3:] != '.py':
                continue
            packageSet = __import__( module[:-3], locals(), globals() )
            for name, obj in inspect.getmembers( packageSet ):
                if inspect.isclass( obj ):
                    self.RegisterPackage( obj() )
        return
    def RegisterPackage( self, package ):
        """ Add the package to the list of known packages."""
        print "Registering package %s" % package.GetName()
        package.CheckState()
        self._Packages[package.GetName()] = package
        return
    def CheckPackage( self, packageName ):
        """ Check if the package called packageName is installed."""
        if not packageName in self._Packages.keys():
            raise Exception( "Package %s not found" % packageName )
        package = self._Packages[packageName]
        if package.IsInstalled():
            return True
        return False
    def InstallPackage( self, packageName ):
        """ Install the package by package name."""
        if self.CheckPackage( packageName ):
            return
        package = self._Packages[packageName]
        if isinstance( package, CommandPackage.CommandPackage ):
            # Ah user must install this system wide...
            raise Exception( "Package %s must be installed manually." % package.GetName() )
        if isinstance( package, ConditionalPackage.ConditionalPackage ):
            print "Installing %s" % package.GetName()
            package.Install()
            print "Package: %s installed." % package.GetName()
            return
        # Not installed and a LocalPackage, thus can install. Start with dependencies, and build dependency dict
        dependencyPaths = {}
        for dependency in package.GetDependencies(): 
            self.InstallPackage( dependency )
            dependencyPaths[dependency] = self._Packages[dependency].GetInstallPath()
        # Now we can install this package
        package.SetDependencyPaths( dependencyPaths )
        print "Installing %s" % package.GetName()
        package.Install()
        package.CheckState()
        if not package.IsInstalled():
            print "Package: %s, errored during install." % package.GetName()
            return
        print "Package: %s installed." % package.GetName()
        return
    
