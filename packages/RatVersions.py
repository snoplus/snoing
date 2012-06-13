#!/usr/bin/env python
# Author P G Jones - 18/05/2012 <p.g.jones@qmul.ac.uk> : First revision
#        O Wasalski - 05/06/2012 <wasalski@berkeley.edu> : Added curl dependency to RAT-dev and rat-3
#        O Wasalski - 13/06/2012 <waslski@berkeley.edu> : Added bzip2 dependency to rat-dev
# The RAT packages (versions)
import Rat
import os
import PackageUtil
import getpass #Temp RAT-4

class RATDev( Rat.Rat ):
    """ Rat dev install package."""
    def __init__( self ):
        """ Initiliase the rat dev package."""
        super( RATDev, self ).__init__( "rat-dev" )
    def CheckState( self ):
        """ Derived classes should override this to ascertain the package status, downloaded? installed?"""
        if os.path.exists( os.path.join( self.GetInstallPath() ) ):
            self._SetMode( 1 ) # Downloaded
        if os.path.exists( os.path.join( self.GetInstallPath(), "bin/root" ) ): # Temp test method
            self._SetMode( 2 ) # Installed as well
        return
    def GetDependencies( self ):
        """ Return the dependency names as a list of names."""
        return [ "clhep-2.1.0.1", "geant4.9.4.p01", "root-5.32.03", "scons-2.1.0", "avalanche-1", "zeromq-2.2.0", "xerces-c-3.1.1", "curl-7.26.0", "bzip2-1.0.6" ]
    def _Download( self ):
        """ Git clone rat-dev."""
        return PackageUtil.ExecuteSimpleCommand( "git", ["clone", "git@github.com:snoplus/rat.git", self.GetInstallPath()], None, os.getcwd() )
    def _WriteEnvFile( self ):
        """ Write the environment file for rat."""
        outText = """#!/bin/bash
#ratcage environment
source %(Geant)s/env.sh
export ROOTSYS=%(Root)s
export AVALANCHEROOT=%(Avalanche)s
export ZEROMQROOT=%(Zeromq)s
export XERCESCROOT=%(Xercesc)s
export BZ2ROOT=%(Bzip2)s
export PATH=%(Root)s/bin:%(Curl)s/bin:$BZ2ROOT/bin:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:%(Clhep)s/lib:%(Root)s/lib:%(Avalanche)s/lib/cpp:%(Zeromq)s/lib:%(Xercesc)s/lib:$BZ2ROOT/lib
export DYLD_LIBRARY_PATH=$DYLD_LIBRARY_PATH:%(Clhep)s/lib:%(Root)s/lib:%(Avalanche)s/lib/cpp:%(Zeromq)s/lib:%(Xercesc)s/lib:$BZ2ROOT/lib
export PYTHONPATH=%(Root)s/lib:$PYTHONPATH
export RAT_SCONS=%(Scons)s
source %(Rat)s/env.sh""" % { "Geant" : self._DependencyPaths["geant4.9.4.p01"], "Root" : self._DependencyPaths["root-5.32.03"], "Clhep" : self._DependencyPaths["clhep-2.1.0.1"], "Scons" : self._DependencyPaths["scons-2.1.0"], "Rat" : self.GetInstallPath(), "Avalanche" : self._DependencyPaths["avalanche-1"], "Zeromq" : self._DependencyPaths["zeromq-2.2.0"], "Xercesc" : self._DependencyPaths["xerces-c-3.1.1"], "Curl" : self._DependencyPaths["curl-7.26.0"], "Bzip2" : self._DependencyPaths["bzip2-1.0.6"] }
        with open( os.path.join( PackageUtil.kInstallPath, "env_%s.sh" % self._Name ), "w" ) as envFile:
            envFile.write( outText )
        return

class RAT4( Rat.RatReleasePost3 ):
    """ Temporary Rat release-4.00, install package."""
    def __init__( self ):
        """ Initiliase the rat 4.0 package."""
        super( RAT4, self ).__init__( "rat-4", "ProposedPhysicsList", "clhep-2.1.0.1", "geant4.9.5.p01", "root-5.32.03", "scons-2.1.0", "avalanche-1", "zeromq-2.2.0", "xerces-c-3.1.1", "curl-7.26.0" )
        return
    def _Download( self ):
        """ Derived classes should override this to download the package. Return True on success."""
        if self._Username is None:
            self._Username = raw_input( "Github username:" )
        if self._Password is None:
            print "Github password:"
            self._Password = getpass.getpass()
        return PackageUtil.DownloadFile( "https://github.com/pgjones/rat/tarball/ProposedPhysicsList", self._Username, self._Password )
    def _WriteEnvFile( self ):
        """ Write the environment file for rat."""
        outText = """#!/bin/bash
#ratcage environment
source %(Geant)s/bin/geant4.sh
export ROOTSYS=%(Root)s
export AVALANCHEROOT=%(Avalanche)s
export ZEROMQROOT=%(Zeromq)s
export XERCESCROOT=%(Xercesc)s
export PATH=%(Root)s/bin:%(Geant)s/bin:%(Curl)s/bin:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:%(Clhep)s/lib:%(Root)s/lib:%(Avalanche)s/lib/cpp:%(Zeromq)s/lib:%(Xercesc)s/lib
export DYLD_LIBRARY_PATH=$DYLD_LIBRARY_PATH:%(Clhep)s/lib:%(Root)s/lib:%(Avalanche)s/lib/cpp:%(Zeromq)s/lib:%(Xercesc)s/lib
export PYTHONPATH=%(Root)s/lib:$PYTHONPATH
export RAT_SCONS=%(Scons)s
source %(Rat)s/env.sh""" % { "Geant" : self._DependencyPaths[self._GeantDependency], "Root" : self._DependencyPaths[self._RootDependency], "Clhep" : self._DependencyPaths[self._ClhepDependency], "Scons" : self._DependencyPaths[self._SconsDependency], "Rat" : self.GetInstallPath(), "Avalanche" : self._DependencyPaths[self._AvalancheDependency], "Zeromq" : self._DependencyPaths[self._ZeromqDependency], "Xercesc" : self._DependencyPaths[self._XercescDependency], "Curl" : self._DependencyPaths["curl-7.26.0"] }
        with open( os.path.join( PackageUtil.kInstallPath, "env_%s.sh" % self._Name ), "w" ) as envFile:
            envFile.write( outText )
        return

class RAT3( Rat.RatReleasePost3 ):
    """ Rat release-3.00, install package."""
    def __init__( self ):
        """ Initiliase the rat 3.0 package."""
        super( RAT3, self ).__init__( "rat-3", "release-3.00", "clhep-2.1.0.1", "geant4.9.4.p01", "root-5.32.03", "scons-2.1.0", "avalanche-1", "zeromq-2.2.0", "xerces-c-3.1.1", "curl-7.26.0" )
        return

class RAT2( Rat.RatReleasePre3 ):
    """ Rat release-2.00, install package."""
    def __init__( self ):
        """ Initiliase the rat 2.0 package."""
        super( RAT2, self ).__init__( "rat-2", "release-2.00", "clhep-2.1.0.1", "geant4.9.4.p01", "root-5.28.00", "scons-2.1.0" )
        return

class RAT1( Rat.RatReleasePre3 ):
    """ Rat release-1.00, install package."""
    def __init__( self ):
        """ Initiliase the rat 1.0 package."""
        super( RAT1, self ).__init__( "rat-1", "release-1.00", "clhep-2.0.4.2", "geant4.9.2.p02", "root-5.24.00", "scons-1.2.0" )
        return

class RAT0( Rat.RatReleasePre3 ):
    """ Rat release-0.00, install package."""
    def __init__( self ):
        """ Initiliase the rat 0.0 package."""
        super( RAT0, self ).__init__( "rat-0", "release-0.00", "clhep-2.0.4.2", "geant4.9.2.p02", "root-5.24.00", "scons-1.2.0" )
        return

