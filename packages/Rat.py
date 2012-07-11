#!/usr/bin/env python
# Author P G Jones - 16/05/2012 <p.g.jones@qmul.ac.uk> : First revision
#        O Wasalski - 05/06/2012 <wasalski@berkeley.edu> : Added curl dependency to RatReleasePost3
#        P G Jones - 21/06/2012 <p.g.jones@qmul.ac.uk> : Second revision use env file builder, refactored versions
# The RAT packages base class
import LocalPackage
import os
import PackageUtil
import getpass
import EnvFileBuilder

class Rat( LocalPackage.LocalPackage ):
    """ Base rat installer for rat."""
    def __init__( self, name, rootDependency, sconsDependency ):
        """ All Rat installs have the same root and scons dependence."""
        super( Rat, self ).__init__( name, False ) # Not graphical only
        self._EnvFile = EnvFileBuilder.EnvFileBuilder( "#ratcage environment\n" )
        self._RootDependency = rootDependency
        self._SconsDependency = sconsDependency
        return

    def GetDependencies( self ):
        """ Return the dependency names as a list of names."""
        dependencies = [ "python", "python-dev", self._SconsDependency, self._RootDependency ]
        dependencies.extend( self._GetDependencies() )
        return dependencies
    def _IsDownloaded( self ):
        """ Check if downloaded, git-cloned or tar file downloaded."""
        pass
    def _IsInstalled( self ):
        """ Rat releases and dev share a common install check."""
        # Check rat, root, RATLib and RATDSLib
        sys = os.uname()[0]
        return os.path.exists( os.path.join( self.GetInstallPath(), "bin/rat_%s-g++" % sys ) ) \
            and os.path.exists( os.path.join( self.GetInstallPath(), "bin/root" ) ) \
            and PackageUtil.LibraryExists( os.path.join( self.GetInstallPath(), "lib" ), "librat_%s-g++" % sys ) \
            and PackageUtil.LibraryExists( os.path.join( self.GetInstallPath(), "lib" ), "libRATEvent_%s-g++" % sys )
    def _Download( self ):
        """ Dependends on rat type."""
        pass
    def _Install( self ):
        """ Derived classes should override this to install the package, should install only when finished. Return True on success."""
        self.WriteEnvFile()
        # Write the command file and source it...
        commandText = """#!/bin/bash\nsource %s\ncd %s\n./configure\nsource env.sh\nscons""" % ( os.path.join( PackageUtil.kInstallPath, "env_%s.sh" % self._Name ), self.GetInstallPath() )
        self._InstallPipe += PackageUtil.ExecuteComplexCommand( commandText )
        return
    def WriteEnvFile( self ):
        """ Adds general parts and then writes the env file."""
        self._EnvFile.AddEnvironment( "ROOTSYS", self._DependencyPaths[self._RootDependency] )
        self._EnvFile.AddEnvironment( "RAT_SCONS", self._DependencyPaths[self._SconsDependency] )
        self._EnvFile.AppendPythonPath( os.path.join( self._DependencyPaths[self._RootDependency], "lib" ) )
        self._EnvFile.AppendLibraryPath( os.path.join( self._DependencyPaths[self._RootDependency], "lib" ) )
        self._EnvFile.AddFinalSource( self.GetInstallPath(), "env" )
        self._WriteEnvFile()
        self._EnvFile.WriteEnvFiles( PackageUtil.kInstallPath, "env-%s" % self._Name )
        return
    # Functions that must be implemented by sub classes
    def _WriteEnvFile( self ):
        """ Sub classes should add parts to the env file."""
        pass
    def _GetDependencies( self ):
        """ Sub classes should return a list of dependencies."""
        pass

class RatRelease( Rat ):
    """ Base rat installer for rat releases."""
    def __init__( self, name, rootDependency, sconsDependency, tarName ):
        """ Initialise rat with the tarName."""
        super( RatRelease, self ).__init__( name, rootDependency, sconsDependency )
        self._TarName = tarName
        return

    def _IsDownloaded( self ):
        """ Check if tarball has been downloaded."""
        return os.path.exists( os.path.join( PackageUtil.kCachePath, self._TarName ) )
    def _Download( self ):
        """ Derived classes should override this to download the package. Return True on success."""
        if self._Username is None:
            self._Username = raw_input( "Github username:" )
        if self._Password is None:
            print "Github password:"
            self._Password = getpass.getpass()
        self._DownloadPipe += PackageUtil.DownloadFile( "https://github.com/snoplus/rat/tarball/" + self._TarName, \
                                                            self._Username, self._Password )
        return
    def _Install( self ):
        """ Release installs must untar first."""
        self._InstallPipe += PackageUtil.UnTarFile( self._TarName, self.GetInstallPath(), 1 ) # Strip the first directory
        super( RatRelease, self )._Install()
        return
    def SetUsernamePassword( self, username, password ):
        """ Set the username password combination required for github downloads."""
        self._Username = username
        self._Password = password
        return 
