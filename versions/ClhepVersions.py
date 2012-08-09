#!/usr/bin/env python
# Author P G Jones - 13/05/2012 <p.g.jones@qmul.ac.uk> : First revision
# The CLHEP packages (versions)
import Clhep
import PackageUtil

class CLHEP2110( Clhep.Clhep ):
    """ Clhep 2.1.1.0, install package."""
    def __init__( self ):
        """ Initiliase the clhep 2.1.1.0 package."""
        super( CLHEP2110, self ).__init__( "clhep-2.1.1.0", "clhep-2.1.1.0.tgz" )
        return

class CLHEP2101( Clhep.Clhep ):
    """ Clhep 2.1.0.1, install package."""
    def __init__( self ):
        """ Initiliase the clhep 2.1.0.1 package."""
        super( CLHEP2101, self ).__init__( "clhep-2.1.0.1", "clhep-2.1.0.1.tgz" )
        return

class CLHEP2042( Clhep.Clhep ):
    """ Clhep 2.0.4.2, install package."""
    def __init__( self ):
        """ Initiliase the clhep 2.0.4.2 package."""
        super( CLHEP2042, self ).__init__( "clhep-2.0.4.2", "clhep-2.0.4.2.tgz" )
        return
