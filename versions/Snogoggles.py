#!/usr/bin/env python
# Author O Wasalski 
# OW - 07/06/2012 <wasalski@berkeley.edu> : First revision, new file
# The SNOGoggles packages base class
import os
import LocalPackage
import PackageUtil

class Snogoggles( LocalPackage.LocalPackage ):
    """ Snogoggles local package. 
        Installs development version.
    """

    def __init__( self ):
        """ Initializes snogoggles package. """
        super( Snogoggles, self ).__init__( "snogoggles-dev" )
        self._DownloadPath = os.path.join( PackageUtil.kCachePath, self._Name )
        self._Dependencies = { "Scons": "scons-2.1.0",
                               "Geant4": "geant4.9.4.p04",
                               "Rat": "rat-dev",
                               "Root": "root-5.32.03",
                               "Sfml": "sfml-2.0",
                               "Xercesc": "xerces-c-3.1.1",
                               "Avalanche": "avalanche-1",
                               "Zeromq": "zeromq-2.2.0"
                             }


########### "Public" functions - overrides LocalPackage ################

    def CheckState( self ):
        """ Check if downloaded and installed."""
        self._SetMode( 0 )
        mainfile = os.path.join( self._DownloadPath, "SNOGoggles.cc" )
        binary = os.path.join( self.GetInstallPath(), "bin", "snogoggles" )
        if( os.path.isfile( mainfile ) ):
            self._SetMode( 1 )
        if( os.path.isfile( binary ) ):
            self._SetMode( 2 )

    def GetDependencies( self ):
        """ Return the required dependencies."""
        return self._Dependencies.values()

########### "Private" functions - overrides LocalPackage ################

    def _Download( self ):
        """ Derived classes should override this to download the package. 
        Return True on success.""" 
        # Downloads into the cache path
        return PackageUtil.ExecuteComplexCommand( """
            git clone git@github.com:/snoplus/snogoggles.git %s """
            % self._DownloadPath )

    def _Install( self ):
        """ Install the version."""
        import copy
        import shutil

        # Create dependency dictionary with install paths
        d = copy.deepcopy( self._Dependencies )
        for k, v in zip( d.keys(), d.values() ):
            d[k] = self._DependencyPaths[v]
        d["InstallPath"] = self.GetInstallPath()
 
        # Copy directory from cache to install path
        if( not os.path.exists( self.GetInstallPath() ) ):
            shutil.copytree( self._DownloadPath, self.GetInstallPath() )

        # Compile snogoggles
        return PackageUtil.ExecuteComplexCommand( """
            cd %(InstallPath)s
            export RAT_SCONS=%(Scons)s
            export GEANT4_BASE=%(Geant4)s
            export RATROOT=%(Rat)s
            export ROOTSYS=%(Root)s
            export SFMLROOT=%(Sfml)s
            export XERCESCROOT=%(Xercesc)s
            export AVALANCHEROOT=%(Avalanche)s
            export ZEROMQROOT=%(Zeromq)s
            ./autoconfigure
            source env.sh
            scons
            """ % d )


