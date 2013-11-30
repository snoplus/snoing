#!/usr/bin/env python
#
# Geant495, Geant494, Geant492
#
# The geant4 release versions
#
# Author P G Jones - 15/05/2012 <p.g.jones@qmul.ac.uk> : First revision
# Author P G Jones - 22/09/2012 <p.g.jones@qmul.ac.uk> : Major refactor of snoing.
####################################################################################################
import geant4

class Geant496(geant4.Geant4Post5):
    """ Geant4 4.9.6.p02, install package."""
    def __init__(self, system):
        """ Initiliase the geant4 4.9.6.p02 package."""
        super(Geant496, self).__init__("geant4.9.6.p02", system, "geant4.9.6.p02.tar.gz", 
                                       "xerces-c-3.1.1")

class Geant495(geant4.Geant495):
    """ Geant4 4.9.5.p01, install package."""
    def __init__(self, system):
        """ Initiliase the geant4 4.9.5.p01 package."""
        super(Geant495, self).__init__("geant4.9.5.p01", system, "geant4.9.5.p01.tar.gz", 
                                       "clhep-2.1.1.0", "xerces-c-3.1.1")

class Geant494(geant4.Geant4Pre5):
    """ Geant4 4.9.4.p04, install package."""
    def __init__(self, system):
        """ Initiliase the geant4 4.9.4.p04 package."""
        super(Geant494, self).__init__("geant4.9.4.p01", system, "geant4.9.4.p01.tar.gz",
                                       [ "G4NDL.3.14.tar.gz", "G4EMLOW.6.19.tar.gz", 
                                         "G4PhotonEvaporation.2.1.tar.gz", 
                                         "G4RadioactiveDecay.3.3.tar.gz", "G4ABLA.3.0.tar.gz" ], 
                                       "clhep-2.1.0.1", "xerces-c-3.1.1")

class Geant492(geant4.Geant4Pre5):
    """ Geant4 4.9.2.p02, install package."""
    def __init__(self, system):
        """ Initiliase the geant4 4.9.2.p02 package."""
        super(Geant492, self).__init__("geant4.9.2.p02", system, "geant4.9.2.p02.tar.gz",
                                       [ "G4NDL.3.13.tar.gz", "G4EMLOW.6.2.tar.gz", 
                                         "G4PhotonEvaporation.2.0.tar.gz", 
                                         "G4RadioactiveDecay.3.2.tar.gz", "G4ABLA.3.0.tar.gz" ], 
                                       "clhep-2.0.4.2", "xerces-c-3.1.1")
