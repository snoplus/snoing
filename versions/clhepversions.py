#!/usr/bin/env python
#
# CLHEP2110, CLHEP2101, CLHEP2042
#
# The clhep release versions
#
# Author P G Jones - 13/05/2012 <p.g.jones@qmul.ac.uk> : First revision
# Author P G Jones - 22/09/2012 <p.g.jones@qmul.ac.uk> : Major refactor of snoing.
####################################################################################################
import clhep

class CLHEP2110(clhep.Clhep):
    """ Clhep 2.1.1.0, install package."""
    def __init__(self, system):
        """ Initiliase the clhep 2.1.1.0 package."""
        super(CLHEP2110, self).__init__("clhep-2.1.1.0", system, "clhep-2.1.1.0.tgz")

class CLHEP2101(clhep.Clhep):
    """ Clhep 2.1.0.1, install package."""
    def __init__(self, system):
        """ Initiliase the clhep 2.1.0.1 package."""
        super(CLHEP2101, self).__init__("clhep-2.1.0.1", system, "clhep-2.1.0.1.tgz")

class CLHEP2042(clhep.Clhep):
    """ Clhep 2.0.4.2, install package."""
    def __init__(self, system):
        """ Initiliase the clhep 2.0.4.2 package."""
        super(CLHEP2042, self).__init__("clhep-2.0.4.2", system, "clhep-2.0.4.2.tgz")
