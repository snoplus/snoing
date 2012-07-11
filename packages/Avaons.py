#!/usr/bin/env python
# Author P G Jones - 11/07/2012 <p.g.jones@qmul.ac.uk> : First revision
# The Avaons packages base class, allows for multiple avaons versions
import LocalPackage
import os
import PackageUtil
import EnvFileBuilder

class Avaons( LocalPackage.LocalPackage ):
    """ Base avaons installer for avaons."""
    def __init__( self, name, zmqDependency, curlDependency, rootDependency, ratDependency, bzipDependency, avalancheDependency, sconsDependency ):
        """ Initialise avaons with the tarName."""
        super( Avaons, self ).__init__( name, False ) # Not graphical only
        self._ZeromqDependency = zmqDependency
        self._RootDependency = rootDependency
        self._CurlDependency = curlDependency
        self._RatDependency = ratDependency
        self._BZipDependency = bzipDependency
        self._AvalancheDependency = avalancheDependency
        self._SconsDependency = sconsDependency
        return
    def GetDependencies( self ):
        """ Return the required dependencies."""
        return ["python-dev", self._ZeromqDependency, self._CurlDependency, self._RootDependency, self._RatDependency, self._BZipDependency, self._AvalancheDependency, self._SconsDependency]
    def _IsDownloaded( self ):
        """ Check if downloaded."""
        return os.path.exists( self.GetInstallPath() )
    def _Download( self ):
        """ Download avalanche (git clone)."""
        self._DownloadPipe += PackageUtil.ExecuteSimpleCommand( "git", ["clone", "git@github.com:pgjones/Avaons.git",  self.GetInstallPath()], None, os.getcwd() )
        return
    def _IsInstalled( self ):
        """ Check if installed."""
        return os.path.exists( os.path.join( self.GetInstallPath(), "avaons" ) )
    def _Install( self ):
        """ Install Avaons."""
        envFile = EnvFileBuilder.EnvFileBuilder()
        envFile.AppendPath( os.path.join( self._DependencyPaths[self._CurlDependency], "bin" )  )
        envFile.AppendPath( os.path.join( self._DependencyPaths[self._SconsDependency], "script" )  )
        envFile.AppendPythonPath( os.path.join( self._DependencyPaths[self._SconsDependency], "engine" )  )
        envFile.AddEnvironment( "ROOTSYS", self._DependencyPaths[self._RootDependency] )
        envFile.AddEnvironment( "RATROOT", self._DependencyPaths[self._RatDependency] )
        envFile.AddEnvironment( "G4SYSTEM", os.uname()[0] + "-g++" ) # Temp
        if self._DependencyPaths[self._BZipDependency] is not None:
            envFile.AddEnvironment( "BZIPROOT", self._DependencyPaths[self._BZipDependency] )
        envFile.AddEnvironment( "AVALANCHEROOT", self._DependencyPaths[self._AvalancheDependency] )
        envFile.AddEnvironment( "ZEROMQROOT", self._DependencyPaths[self._ZeromqDependency] )
        envFile.WriteEnvFiles( self.GetInstallPath(), "env" )
        commandText = """#!/bin/bash\ncd %s\nsource env.sh\nscons\n""" % self.GetInstallPath() 
        self._InstallPipe += PackageUtil.ExecuteComplexCommand( commandText )
        return
