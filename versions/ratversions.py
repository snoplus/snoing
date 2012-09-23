#!/usr/bin/env python
#
# RATDev, RAT4, RAT3, RAT2, RAT1, RAT0
#
# The rat release versions
#
# Author P G Jones - 18/05/2012 <p.g.jones@qmul.ac.uk> : First revision
#        O Wasalski - 05/06/2012 <wasalski@berkeley.edu> : Added curl dependency to RAT-dev and rat-3
#        O Wasalski - 13/06/2012 <waslski@berkeley.edu> : Added bzip2 dependency to rat-dev
#        P G Jones - 21/06/2012 <p.g.jones@qmul.ac.uk> : New releases usage.
#        P G Jones - 02/08/2012 <p.g.jones@qmul.ac.uk> : Moved rat-dev to geant4.9.5 and updated rat-4
# Author P G Jones - 23/09/2012 <p.g.jones@qmul.ac.uk> : Major refactor of snoing.
####################################################################################################
import rat
import ratreleases
import os

class RATDev(rat.RatDevelopment):
    """ Rat dev install package."""
    def __init__(self, system):
        """ Initiliase the rat dev package."""
        super(RATDev, self).__init__("rat-dev", system)

class RAT4(ratreleases.RatRelease4):
    """ Rat release-4.00, install package."""
    def __init__(self):
        """ Initiliase the rat 4.0 package."""
        super(RAT4, self).__init__("rat-4", "root-5.32.04", "geant4.9.5.p01", "scons-2.1.0", 
                                   "clhep-2.1.1.0", "curl-7.26.0", "bzip2-1.0.6", "avalanche-1", 
                                   "zeromq-2.2.0", "xerces-c-3.1.1", "release-4.00")

class RAT3(ratreleases.RatRelease3):
    """ Rat release-3.00, install package."""
    def __init__(self):
        """ Initiliase the rat 3.0 package."""
        super(RAT3, self).__init__("rat-3", "root-5.32.04", "geant4.9.4.p01", "scons-2.1.0", 
                                   "clhep-2.1.0.1", "curl-7.26.0", "bzip2-1.0.6", "avalanche-1", 
                                   "zeromq-2.2.0", "xerces-c-3.1.1", "release-3.00")

class RAT2(ratreleases.RatRelease2):
    """ Rat release-2.00, install package."""
    def __init__(self):
        """ Initiliase the rat 2.0 package."""
        super(RAT2, self).__init__("rat-2", "root-5.28.00", "geant4.9.4.p01", "scons-2.1.0", 
                                   "clhep-2.1.0.1", "curl-7.26.0", "bzip2-1.0.6", "release-2.00")

class RAT1(ratreleases.RatRelease0and1):
    """ Rat release-1.00, install package."""
    def __init__(self):
        """ Initiliase the rat 1.0 package."""
        super(RAT1, self).__init__("rat-1", "root-5.24.00", "geant4.9.2.p02", "scons-1.2.0", 
                                   "clhep-2.0.4.2", "release-1.00")

class RAT0(ratreleases.RatRelease0and1):
    """ Rat release-0.00, install package."""
    def __init__(self):
        """ Initiliase the rat 0.0 package."""
        super(RAT0, self).__init__("rat-0", "root-5.24.00", "geant4.9.2.p02", "scons-1.2.0", 
                                   "clhep-2.0.4.2", "release-0.00")

