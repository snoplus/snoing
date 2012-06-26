#!/usr/bin/env python
# Author O Wasalski - 07/06/2012 <wasalski@berkeley.edu> : First revision, new file.
# Author P G Jones - 24/06/2012 <p.g.jones@qmul.ac.uk> : Refactor for new package types.
import Sfml

class Sfml20( Sfml.Sfml ):
    """ """

    def __init__( self ):
        """ Initialize the package, set the name."""
        super( Sfml20, self ).__init__( "sfml-2.0", "fa4415cf8a423e0ad3f1c0a84d053ca2d1eef134" )
        return

    
