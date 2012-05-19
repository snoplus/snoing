#!/usr/bin/env python
# Author P G Jones - 18/05/2012 <p.g.jones@qmul.ac.uk> : First revision
# The RAT packages (versions)
import Rat

class RAT2( Rat.RatReleasePre3 ):
    """ Rat release-2.00, install package."""
    def __init__( self, cachePath, installPath, graphical ):
        """ Initiliase the rat 2.0 package."""
        super( RAT2, self ).__init__( "rat-2", cachePath, installPath, "release-2.00", "release-2.00", "clhep-2.1.0.1", "geant4.9.2.p02", "root-5.32.03", "scons-2.1.0" )
        return


