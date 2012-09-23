#!/usr/bin/env python
#
# AvalancheDev, AvalancheV1
#
# The development and release versions of avalanche.
#
# Author P G Jones - 19/05/2012 <p.g.jones@qmul.ac.uk> : First revision
#        O Wasalski - 05/06/2012 <wasalski@berkeley.edu> : Added curl dependency
# Author P G Jones - 23/06/2012 <p.g.jones@qmul.ac.uk> : Major refactor of snoing.
####################################################################################################
import avalanche

class AvalancheDev(avalanche.Avalanche):
    """ The development version of avalanche (git repo)."""
    def __init__(self, system):
        """ Initiliase the dev version."""
        super(AvalancheDev, self).__init__("avalanche-dev", system, "zeromq-2.2.0", 
                                           "root-5.32.04", "curl-7.26.0")
    def _IsDownloaded( self ):
        """ Check if downloaded."""
        return self._system.file_exists(self.get_install_path())
    def _Download( self ):
        """ Download avalanche (git clone)."""
        args = ["clone", "git@github.com:mastbaum/avalanche.git",  self.get_install_path()]
        self._system.execute_command("git", args)

class AvalancheV1(avalanche.AvalancheRelease):
    def __init__(self, system):
        """ Initialise version 1."""
        super(AvalancheV1, self).__init__("avalanche-1", system, "zeromq-2.2.0", 
                                          "root-5.32.04", "curl-7.26.0", 
                                          "d400c35640413a1b017bcd93a926e354c7aaaaff")
