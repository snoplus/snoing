#!/usr/bin/env python
#
# AvalancheDev
#
# The development and release versions of avalanche.
#
# Author P G Jones - 19/05/2012 <p.g.jones@qmul.ac.uk> : First revision
#        O Wasalski - 05/06/2012 <wasalski@berkeley.edu> : Added curl dependency
# Author P G Jones - 23/06/2012 <p.g.jones@qmul.ac.uk> : Major refactor of snoing.
####################################################################################################
import avalanche

class AvalancheDev(avalanche.Avalanche):
    def __init__(self, system):
        """ Initialise dev version."""
        super(AvalancheDev, self).__init__("avalanche-dev", system, "root-5.32.04")
