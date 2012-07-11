#!/usr/bin/env python
# Author P G Jones - 19/05/2012 <p.g.jones@qmul.ac.uk> : First revision
#        O Wasalski - 05/06/2012 <wasalski@berkeley.edu> : Added curl dependency
# The Avalanche package
import Avalanche
import os
import PackageUtil

class AvalancheDev( Avalanche.Avalanche ):
    """ The development version of avalanche (git repo)."""
    def __init__( self ):
        """ Initiliase the dev version."""
        super( AvalancheDev, self ).__init__( "avalanche-dev", "zeromq-2.2.0", "root-5.32.03", "curl-7.26.0" )
        return
    def _IsDownloaded( self ):
        """ Check if downloaded."""
        return os.path.exists( self.GetInstallPath() )
    def _Download( self ):
        """ Download avalanche (git clone)."""
        self._DownloadPipe += PackageUtil.ExecuteSimpleCommand( "git", ["clone", "git@github.com:mastbaum/avalanche.git",  self.GetInstallPath()], None, os.getcwd() )
        return

class AvalancheV1( Avalanche.AvalancheRelease ):
    def __init__( self ):
        """ Initialise version 1."""
        super( AvalancheV1, self ).__init__( "avalanche-1", "zeromq-2.2.0", "root-5.32.03", "curl-7.26.0", "d400c35640413a1b017bcd93a926e354c7aaaaff" )
        return
