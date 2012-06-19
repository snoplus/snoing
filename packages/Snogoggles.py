#!/usr/bin/env python
# Author O Wasalski 
# OW - 07/06/2012 <wasalski@berkeley.edu> : First revision, new file
# The SNOGoggles packages base class
import os
import LocalPackage
import PackageUtil

class Snogoggles( LocalPackage.LocalPackage ):
    """ """

    def __init__( self ):
        """ """
        super( Snogoggles, self ).__init__( "snogoggles-dev" )
        self._Dependencies = { "Scons": "scons-2.1.0",
                               "Geant4": "geant4.9.4.p01",
                               "Rat": "rat-dev",
                               "Root": "root-5.32.03",
                               "Sfml": "sfml-2.0",
                               "Xercesc": "xerces-c-3.1.1",
                               "Avalanche": "avalanche-1",
                               "Zeromq": "zeromq-2.2.0"
                             }
        return

########### "Public" functions - overrides LocalPackage ################

    def CheckState( self ):
        """ Check if downloaded and installed."""
        self._SetMode( 0 )
        if( self._Downloaded() ):
            self._SetMode( 1 )
        if( self._Installed() ):
            self._SetMode( 2 )

    def GetDependencies( self ):
        """ Return the required dependencies."""
        return self._Dependencies.values()

########### "Private" functions - overrides LocalPackage ################

    def _Download( self ):
        """ Derived classes should override this to download the package. 
        Return True on success.""" 
        PackageUtil.ExecuteSimpleCommand( "git", 
            [ "clone", "git@github.com:snoplus/snogoggles.git", 
            self.GetInstallPath() ], None, os.getcwd() )
        return self._Downloaded()

    def _Install( self ):
        """ Install the version."""
        import copy
        installPath = self.GetInstallPath()
        configPath = os.path.join( installPath, "config" )

        d = copy.deepcopy( self._Dependencies )
        for k, v in zip( d.keys(), d.values() ):
            d[k] = self._DependencyPaths[v]

        for fName in [ "env.sh", "env.csh" ]:
            fIn = open( os.path.join( configPath, fName ), "r" )
            fOut = open( os.path.join( installPath, fName ), "w" )
            fOut.write( fIn.read() % d )
            fIn.close()
            fOut.close()

        PackageUtil.ExecuteComplexCommand( "cd %s && source env.sh && scons" %installPath )
        
        return self._Installed()

########### "Private" functions - helper for this class only ################

    def _Downloaded( self ):
        mainFile = os.path.join( self.GetInstallPath(), "SNOGoggles.cc" )
        return os.path.isfile( mainFile )

    def _Installed( self ):
        return False



