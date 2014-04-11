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

class Xsnoed510(xsnoed.XsnoedRelease):
    """ Xsnoed release 5.1.0, install package."""
    def __init__(self, system):
        """ Initiliase the xsnoed 5.1.0 package."""
        super(Xsnoed510, self).__init__("xsnoed-5.1.0", system, "root-5.34.18", "geant4.9.6.p02",
                                        "rat-4.5.0", "rattools-4.5.0", "v5.1.0")

class Xsnoed502(xsnoed.XsnoedRelease):
    """ Xsnoed release 5.0.2, install package."""
    def __init__(self, system):
        """ Initiliase the xsnoed 5.0.2 package."""
        super(Xsnoed502, self).__init__("xsnoed-5.0.2", system, "root-5.34.11", "geant4.9.6.p02",
                                        "rat-4.5.0", "rattools-4.5.0", "6a7a9d9f5d956c9b89bd01654f242bf26ca0f7de")
