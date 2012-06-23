#!/usr/bin/env python
# Author P G Jones - 23/06/2012 <p.g.jones@qmul.ac.uk> : First revision
# The Curl prerequisites
import LibraryPackage

class Uuid( LibraryPackage.LibraryPackage ):
    """ Package for the universal ids, needed by curl development library."""
    def __init__( self ):
        super( Uuid, self ).__init__( "uuid", "Install uuid-dev on this system.", "uuid", "uuid/uuid.h" )
        return
