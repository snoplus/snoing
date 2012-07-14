#!/usr/bin/env python
# Author P G Jones - 12/05/2012 <p.g.jones@qmul.ac.uk> : First revision
# Base class package manager
import SystemPackage
import LocalPackage
import os
import inspect
import Log
import PackageException
import PackageUtil
import shutil

class PackageManager( object ):
    """ Manages a dictionary of packages that the software can install."""
    def __init__( self ):
        """ Initialise the package manager."""
        self._Packages = {}
        return
    def PackageNameGenerator( self ):
        for packageName in self._Packages:
            yield packageName
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
        Log.Info( "Registering package %s" % package.GetName() )
        package.CheckState()
        self._Packages[package.GetName()] = package
        return
    def CheckPackage( self, packageName ):
        """ Check if the package called packageName is installed."""
        if not packageName in self._Packages.keys():
            Log.Error( "Package %s not found" % packageName )
        package = self._Packages[packageName]
        Log.Info( "Checking package %s install status" % packageName )
        if package.IsInstalled():
            Log.Result( "Installed" )
            return True
        Log.Warn( "Not Installed" )
        return False
    def InstallPackageDependencies( self, packageName ):
        """ Install the package dependencies and not the package."""
        package = self._Packages[packageName]
        for dependency in package.GetDependencies():
            self.InstallPackage( dependency )
        return
    def InstallPackage( self, packageName ):
        """ Install the package by package name."""
        if self.CheckPackage( packageName ):
            return
        package = self._Packages[packageName]
        # If here then not installed :(
        if isinstance( package, SystemPackage.SystemPackage ):
            # Nothing else to do thus return...
            Log.Error( "Package %s must be installed on this system, snoing cannot do this." % package.GetName() )
            Log.Detail( package.GetHelpText() )
            raise Exception()
        # Abort if package is a graphical only package and this is not a graphical install
        if isinstance( package, LocalPackage.LocalPackage ):
            if package.IsGraphicalOnly() and not PackageUtil.kGraphical:
                Log.Error( "Package %s can only be installed in a graphical install." % package.GetName() )
                raise Exception()
        # Not installed and a LocalPackage, thus can install. Start with dependencies, and build dependency dict
        dependencyPaths = {}
        for dependency in package.GetDependencies(): 
            self.InstallPackage( dependency )
            if not isinstance( self._Packages[dependency], SystemPackage.SystemPackage ):
                dependencyPaths[dependency] = self._Packages[dependency].GetInstallPath()
        # All dependencies installed, now we can install this package
        package.SetDependencyPaths( dependencyPaths )
        Log.Info( "Installing %s" % package.GetName() )
        try:
            package.Install()
        except PackageException.PackageException, e:
            Log.Warn( e.Pipe )
        package.CheckState()
        if not package.IsInstalled():
            Log.Error( "Package: %s, errored during install." % package.GetName() )
            raise Exception()
        Log.kLogFile.Write( "Package: %s installed.\n" % package.GetName() )
        Log.Result( "Package: %s installed." % package.GetName() )
        return
    def RemovePackage( self, packageName ):
        """ Remove the package called packageName."""
        if not self.CheckPackage( packageName ):
            return
        package = self._Packages[packageName]
        if isinstance( package, SystemPackage.SystemPackage ): # Don't try to delete system packages
            return
        # First check no other package is dependent on it
        for testPackageName in self.PackageNameGenerator():
            testPackage = self._Packages[testPackageName]
            if isinstance( testPackage, SystemPackage.SystemPackage ): # Ignore system packages
                continue
            if testPackage.IsInstalled():
                if packageName in testPackage.GetDependencies():
                    Log.Error( "Cannot remove %s as %s depends on it." % ( packageName, testPackageName ) )
                    raise Exception()
        # Now delete the package
        Log.Info( "Deleted %s" % packageName )
        shutil.rmtree( package.GetInstallPath() )
        return
                
