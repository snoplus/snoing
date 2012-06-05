#!/usr/bin/env python
# Author O Wasalski - 05/06/2012 <wasalski@berkeley.edu> : First revision, new file.
import Curl

class Curl7260( Curl.Curl ):
    """ Package for curl. """

    def __init__( self ):
        """ Initialize the package, set the name."""
        super( Curl7260, self ).__init__( "curl-7.26.0" )
        return

    
