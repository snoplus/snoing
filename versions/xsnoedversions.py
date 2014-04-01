#!/usr/bin/env python
#
# XsnoedDev, Xsnoed1
#
# The xsnoed release versions
#
# Author P G Jones - 2014-02-03 <p.g.jones@qmul.ac.uk> : First revision
####################################################################################################
import xsnoed

class XsnoedDev(xsnoed.XsnoedDevelopment):
    """ Xsnoed dev install package."""
    def __init__(self, system):
        """ Initiliase the xsnoed dev package."""
        super(XsnoedDev, self).__init__("xsnoed-dev", system)

class Xsnoed502(xsnoed.XsnoedRelease):
    """ Xsnoed release 5.0.2, install package."""
    def __init__(self, system):
        """ Initiliase the xsnoed 5.0.2 package."""
        super(Xsnoed502, self).__init__("xsnoed-5.0.2", system, "root-5.34.11", "geant4.9.6.p02",
                                        "rat-4.5.0", "rattools-4.5.0", "5.0.2")
