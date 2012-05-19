#!/usr/bin/env python
# Author P G Jones - 18/05/2012 <p.g.jones@qmul.ac.uk> : First revision
# The RAT packages (versions)
import Rat

class RAT2( Rat.RatReleasePre3 ):
    """ Rat release-2.00, install package."""
    def __init__( self, cachePath, installPath, graphical ):
        """ Initiliase the rat 2.0 package."""
        super( RAT2, self ).__init__( "rat-2", cachePath, installPath, "release-2.00", "clhep-2.1.0.1", "geant4.9.4.p02", "root-5.28.00", "scons-2.1.0" )
        return

class RAT1( Rat.RatReleasePre3 ):
    """ Rat release-1.00, install package."""
    def __init__( self, cachePath, installPath, graphical ):
        """ Initiliase the rat 1.0 package."""
        super( RAT1, self ).__init__( "rat-1", cachePath, installPath, "release-1.00", "clhep-2.0.4.2", "geant4.9.2.p02", "root-5.24.00", "scons-1.2.0" )
        return

class RAT0( Rat.RatReleasePre3 ):
    """ Rat release-0.00, install package."""
    def __init__( self, cachePath, installPath, graphical ):
        """ Initiliase the rat 0.0 package."""
        super( RAT0, self ).__init__( "rat-0", cachePath, installPath, "release-0.00", "clhep-2.0.4.2", "geant4.9.2.p02", "root-5.24.00", "scons-1.2.0" )
        return

