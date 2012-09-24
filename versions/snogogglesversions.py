#!/usr/bin/env python
#
# SnogogglesDev
#
# The snogoggles release versions
#
# OW - 07/06/2012 <wasalski@berkeley.edu> : First revision, new file
# Author P G Jones - 24/06/2012 <p.g.jones@qmul.ac.uk> : Refactor for new package types.
# Author P G Jones - 27/07/2012 <p.g.jones@qmul.ac.uk> : Added snogoggles versions.
# Author P G Jones - 24/09/2012 <p.g.jones@qmul.ac.uk> : Major refactor of snoing.
####################################################################################################
import snogoggles

class SnogogglesDev(snogoggles.Snogoggles):
    """ Installs development version. """
    def __init__(self, system):
        """ Initializes snogoggles package. """
        super(SnogogglesDev, self).__init__("snogoggles-dev", system, "scons-2.1.0", 
                                            "geant4.9.5.p01", "clhep-2.1.1.0", "rat-dev", 
                                            "root-5.32.04", "sfml-2.0-rc", "xerces-c-3.1.1", 
                                            "avalanche-1", "zeromq-2.2.0", "curl-7.26.0", 
                                            "bzip2-1.0.6")
