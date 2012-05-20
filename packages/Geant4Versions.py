#!/usr/bin/env python
# Author P G Jones - 15/05/2012 <p.g.jones@qmul.ac.uk> : First revision
# The GEANT4 packages (versions)
import Geant4

class GEANT494( Geant4.Geant4Pre5 ):
    """ Geant4 4.9.4.p04, install package."""
    def __init__( self, cachePath, installPath, graphical ):
        """ Initiliase the geant4 4.9.4.p02 package."""
        super( GEANT494, self ).__init__( "geant4.9.4.p01", cachePath, installPath, graphical, "geant4.9.4.p01.tar.gz",
                                          [ "G4NDL.3.14.tar.gz", "G4EMLOW.6.19.tar.gz", "G4PhotonEvaporation.2.1.tar.gz", 
                                            "G4RadioactiveDecay.3.3.tar.gz", "G4ABLA.3.0.tar.gz" ], 
                                          "clhep-2.1.0.1", "xerces-c-3.1.1" )
        return

class GEANT492( Geant4.Geant4Pre5 ):
    """ Geant4 4.9.2.p02, install package."""
    def __init__( self, cachePath, installPath, graphical ):
        """ Initiliase the geant4 4.9.2.p02 package."""
        super( GEANT492, self ).__init__( "geant4.9.2.p02", cachePath, installPath, graphical, "geant4.9.2.p02.tar.gz",
                                          [ "G4NDL.3.13.tar.gz", "G4EMLOW.6.2.tar.gz", "G4PhotonEvaporation.2.0.tar.gz", 
                                            "G4RadioactiveDecay.3.2.tar.gz", "G4ABLA.3.0.tar.gz" ], 
                                          "clhep-2.0.4.2", "xerces-c-3.1.1" )
        return

