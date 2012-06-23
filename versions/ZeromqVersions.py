#!/usr/bin/env python
# Author P G Jones - 19/05/2012 <p.g.jones@qmul.ac.uk> : First revision
# The ZMQ conditional package
import Zeromq

class Zeromq220( Zeromq.Zeromq ):
    """ Zeromq220 install package."""
    def __init__( self ):
        """ Initlaise the ZMQ packages."""
        super( Zeromq220, self ).__init__( "zeromq-2.2.0", "zeromq-2.2.0.tar.gz" )
        return
