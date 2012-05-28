#!/usr/bin/env python
# Author P G Jones - 18/05/2012 <p.g.jones@qmul.ac.uk> : First revision
# The RAT packages (versions)
import Rat
import os
import PackageUtil

class RATDev( Rat.Rat ):
    """ Rat dev install package."""
    def __init__( self, cachePath, installPath, graphical ):
        """ Initiliase the rat dev package."""
        super( RATDev, self ).__init__( "rat-dev", cachePath, installPath, graphical )
    def CheckState( self ):
        """ Derived classes should override this to ascertain the package status, downloaded? installed?"""
        if os.path.exists( os.path.join( self.GetInstallPath() ) ):
            self._SetMode( 1 ) # Downloaded
        if os.path.exists( os.path.join( self.GetInstallPath(), "bin/rat_exe" ) ):
            self._SetMode( 2 ) # Installed as well
        return
    def GetDependencies( self ):
        """ Return the dependency names as a list of names."""
        return [ "clhep-2.1.0.1", "geant4.9.4.p01", "root-5.32.03", "scons-2.1.0", "avalanche-1", "zeromq-2.2.0", "xerces-c-3.1.1" ]
    def _Download( self ):
        """ Git clone rat-dev."""
        return PackageUtil.ExecuteSimpleCommand( "git", ["clone", "git://github.com/snoplus/rat.git", self.GetInstallPath()], None, os.getcwd() )
    def _WriteEnvFile( self ):
        """ Write the environment file for rat."""
        outText = """#!/bin/bash
#ratcage environment
source %(Geant)s/env.sh
export ROOTSYS=%(Root)s
export AVALANCHEROOT=%(Avalanche)s
export ZEROMQROOT=%(Zeromq)s
export XERCESCROOT=%(Xercesc)s
export PATH=%(Root)s/bin:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:%(Clhep)s/lib:%(Root)s/lib:%(Avalanche)s/lib/cpp:%(Zeromq)s/lib:%(Xercesc)s/lib
export DYLD_LIBRARY_PATH=$DYLD_LIBRARY_PATH:%(Clhep)s/lib:%(Root)s/lib:%(Avalanche)s/lib/cpp:%(Zeromq)s/lib:%(Xercesc)s/lib
export PYTHONPATH=%(Root)s/lib:$PYTHONPATH
export RAT_SCONS=%(Scons)s
source %(Rat)s/env.sh""" % { "Geant" : self._DependencyPaths["geant4.9.4.p01"], "Root" : self._DependencyPaths["root-5.32.03"], "Clhep" : self._DependencyPaths["clhep-2.1.0.1"], "Scons" : self._DependencyPaths["scons-2.1.0"], "Rat" : self.GetInstallPath(), "Avalanche" : self._DependencyPaths["avalanche-1"], "Zeromq" : self._DependencyPaths["zeromq-2.2.0"], "Xercesc" : self._DependencyPaths["xerces-c-3.1.1"] }
        with open( os.path.join( self._InstallPath, "env_%s.sh" % self._Name ), "w" ) as envFile:
            envFile.write( outText )
        return

class RAT3( Rat.RatReleasePost3 ):
    """ Rat release-3.00, install package."""
    def __init__( self, cachePath, installPath, graphical ):
        """ Initiliase the rat 3.0 package."""
        super( RAT3, self ).__init__( "rat-3", cachePath, installPath, "release-3.00", "clhep-2.1.0.1", \
                                          "geant4.9.4.p01", "root-5.32.03", "scons-2.1.0", "avalanche-1", "zeromq-2.2.0", "xerces-c-3.1.1" )
        return

class RAT2( Rat.RatReleasePre3 ):
    """ Rat release-2.00, install package."""
    def __init__( self, cachePath, installPath, graphical ):
        """ Initiliase the rat 2.0 package."""
        super( RAT2, self ).__init__( "rat-2", cachePath, installPath, "release-2.00", "clhep-2.1.0.1", "geant4.9.4.p01", "root-5.28.00", "scons-2.1.0" )
        return

class RAT1( Rat.RatReleasePre3 ):
    """ Rat release-1.00, install package."""
    def __init__( self, cachePath, installPath, graphical ):
        """ Initiliase the rat 1.0 package."""
        super( RAT1, self ).__init__( "rat-1", cachePath, installPath, "release-1.00", "clhep-2.0.4.2", "geant4.9.2.p02", "root-5.24.00", "scons-1.2.0" )
        return

class RAT0( Rat.RatReleasePre3 ):
    """ Rat release-0.00, install package."""
    def __init__( self, cachePath, installPath, graphical ):
        """ Initiliase the rat 0.0 package."""
        super( RAT0, self ).__init__( "rat-0", cachePath, installPath, "release-0.00", "clhep-2.0.4.2", "geant4.9.2.p02", "root-5.24.00", "scons-1.2.0" )
        return

