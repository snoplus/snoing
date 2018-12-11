#!/usr/bin/env python
#
# XsnoedDev
#
# The xsnoed release versions
#
# Author P G Jones - 2014-02-03 <p.g.jones@qmul.ac.uk> : First revision
# Author K E Gilje - 2018-09-07 <gilje@ualberta.ca> : Removing all but (working) dev version
####################################################################################################
import xsnoed

class XsnoedDev(xsnoed.XsnoedDevelopment):
    """ Xsnoed dev install package."""
    def __init__(self, system):
        """ Initiliase the xsnoed dev package."""
        super(XsnoedDev, self).__init__("xsnoed-dev", system)

# Commented out to retain format if/when a working version gets released.
#class Xsnoed530(xsnoed.XsnoedRelease):
#    """ Xsnoed release 5.3.0, install package."""
#    def __init__(self, system):
#        """ Initiliase the xsnoed 5.3.0 package."""
#        super(Xsnoed530, self).__init__("xsnoed-5.3.0", system, "root-5.34.36", "geant4.10.0.p02",
#                                        "rat-6.16.0", "rattools-6.16.0", "v5.3.0")
