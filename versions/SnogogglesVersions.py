#!/usr/bin/env python
# Author O Wasalski 
# OW - 07/06/2012 <wasalski@berkeley.edu> : First revision, new file
# Author P G Jones - 24/06/2012 <p.g.jones@qmul.ac.uk> : Refactor for new package types.
# The SNOGoggles packages
import Snogoggles

class SnogogglesDev( Snogoggles.Snogoggles ):
    """ Installs development version. """

    def __init__( self ):
        """ Initializes snogoggles package. """
        super( SnogogglesDev, self ).__init__( "snogoggles-dev", "scons-2.1.0", "geant4.9.4.p01", "rat-dev", "root-5.32.03", "sfml-2.0", "xerces-c-3.1.1", "avalanche-1", "zeromq-2.2.0" )
        return
