#!/usr/bin/env python
# Author P G Jones - 19/05/2012 <p.g.jones@qmul.ac.uk> : First revision
# The Xerces-c conditional package
import XercesC

class XercesC311( XercesC.XercesC ):
    """ XercesC 3.1.1 version."""
    def __init__( self ):
        super( XercesC311, self ).__init__( "xerces-c-3.1.1", "xerces-c-3.1.1.tar.gz" )
        return
