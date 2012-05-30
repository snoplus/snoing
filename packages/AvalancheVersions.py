#!/usr/bin/env python
# Author P G Jones - 19/05/2012 <p.g.jones@qmul.ac.uk> : First revision
# The Avalanche package
import Avalanche

class AvalancheV1( Avalanche.Avalanche ):
    def __init__( self ):
        """ Initialise version 1."""
        super( AvalancheV1, self ).__init__( "avalanche-1", "d400c35640413a1b017bcd93a926e354c7aaaaff", "zeromq-2.2.0", "root-5.32.03" )
        return
