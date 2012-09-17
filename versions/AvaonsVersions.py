#!/usr/bin/env python
# Author P G Jones - 11/07/2012 <p.g.jones@qmul.ac.uk> : First revision
# The Avaons package
import Avaons
import os

class AvaonsDev( Avaons.Avaons ):
    """ The development version of avaons (git repo)."""
    def __init__( self ):
        """ Initiliase the dev version."""
        super( AvaonsDev, self ).__init__( "avaons-dev", "zeromq-2.2.0", "curl-7.26.0", "root-5.32.04", "rat-dev", "bzip2-1.0.6", "avalanche-dev", "scons-2.1.0" )
        return
