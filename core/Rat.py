#!/usr/bin/env python
# Author P G Jones - 16/05/2012 <p.g.jones@qmul.ac.uk> : First revision
# The RAT packages base class
import LocalPackage
import os
import PackageUtil

class RatReleasePre3( LocalPackage.LocalPackage ):
    """ Base rat installer for releases pre 3.0."""
    def __init__( self, name, cachePath, installPath, tarName, clhepDependency, geantDependency, rootDependency, sconsDependency ):
        """ Initialise the rat package."""
        super( RatReleasePre3, self ).__init__( name, cachePath, installPath, False )
        self._TarName = tarName
        self._ClhepDependency = clhepDependency
        self._GeantDependency = geantDependency
        self._RootDependency = rootDependency
        self._SconsDependency = sconsDependency
        return
    # Functions to override
    def CheckState( self ):
        """ Derived classes should override this to ascertain the package status, downloaded? installed?"""
        if os.path.exists( os.path.join( self._CachePath, self._TarName ) ):
            self._SetMode( 1 ) # Downloaded 
        if os.path.exists( os.path.join( self.GetInstallPath(), "bin/rat_exe" ) ):
            self._SetMode( 2 ) # Installed as well
        return
    def GetDependencies( self ):
        """ Return the dependency names as a list of names."""
        return [ self._ClhepDependency, self._GeantDependency, self._RootDependency, self._SconsDependency ]
    def SetUsernamePassword( self, username, password ):
        """ Set the username password combination required for github downloads."""
        self._Username = username
        self._Password = password
        return 
    def _Download( self ):
        """ Derived classes should override this to download the package. Return True on success."""
        return PackageUtil.DownloadFile( "https://github.com/snoplus/rat/tarball/" + self._TarName, self._Username, self._Password )
    def _Install( self ):
        """ Derived classes should override this to install the package, should install only when finished. Return True on success."""
        PackageUtil.UnTarFile( self._TarName, self.GetInstallPath(), 1 ) # Strip the first directory
        self._WriteEnvFile()
        # Write the command file and source it...
        commandText = """#!/bin/bash
source %s
cd %s
./configure
source env.sh
scons""" % ( os.path.join( self._InstallPath, "env_%s.sh" % self._Name ), self.GetInstallPath() )
        return PackageUtil.ExecuteComplexCommand( commandText )
    def _WriteEnvFile( self ):
        """ Write the environment file for rat."""
        outText = """#!/bin/bash
#ratcage environment
source %(Geant)s/env.sh
export ROOTSYS=%(Root)s
export PATH=%(Root)s/bin:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:%(Clhep)s/lib:%(Root)s/lib
export DYLD_LIBRARY_PATH=$DYLD_LIBRARY_PATH:%(Clhep)s/lib:%(Root)s/lib
export PYTHONPATH=%(Root)s/lib:$PYTHONPATH
export RAT_SCONS=%(Scons)s
source %(Rat)s/env.sh""" % { "Geant" : self._DependencyPaths[self._GeantDependency], "Root" : self._DependencyPaths[self._RootDependency], "Clhep" : self._DependencyPaths[self._ClhepDependency], "Scons" : self._DependencyPaths[self._SconsDependency], "Rat" : self.GetInstallPath() }
        envFile = open( os.path.join( self._InstallPath, "env_%s.sh" % self._Name ), "w" )
        envFile.write( outText )
        envFile.close()
        
