#!/usr/bin/env python
# Author O Wasalski - 13/06/2012 <wasalski@berkeley.edu> : First revision
# The bzip2 conditional package
import Bzip2

class Bzip2106( Bzip2.Bzip2 ):
    """ bzip2-1.0.6 install package."""
    def __init__(self):
        """ Initialize the bzip2 package."""
        super( Bzip2106, self ).__init__( "bzip2-1.0.6", "bzip2-1.0.6.tar.gz" )
        return
