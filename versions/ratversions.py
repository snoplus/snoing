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


class RATDev(rat.RatDevelopment):
    """ Rat dev install package."""
    def __init__(self, system):
        """ Initiliase the rat dev package."""
        super(RATDev, self).__init__("rat-dev", system)


class RAT623(ratreleases.RatRelease6):
    """ Rat release-6.2.3, install package."""
    def __init__(self, system):
        """ Initiliase the rat 6.2.3 package."""
        super(RAT623, self).__init__("rat-6.2.3", system, "root-5.34.36", "6.2.3")


class RAT622(ratreleases.RatRelease6):
    """ Rat release-6.2.2, install package."""
    def __init__(self, system):
        """ Initiliase the rat 6.2.2 package."""
        super(RAT622, self).__init__("rat-6.2.2", system, "root-5.34.36", "6.2.2")


class RAT621(ratreleases.RatRelease6):
    """ Rat release-6.2.1, install package."""
    def __init__(self, system):
        """ Initiliase the rat 6.2.1 package."""
        super(RAT621, self).__init__("rat-6.2.1", system, "root-5.34.36", "6.2.1")


class RAT620(ratreleases.RatRelease6):
    """ Rat release-6.2.0, install package."""
    def __init__(self, system):
        """ Initiliase the rat 6.2.0 package."""
        super(RAT620, self).__init__("rat-6.2.0", system, "root-5.34.36", "6.2.0")


class RAT614(ratreleases.RatRelease6):
    """ Rat release-6.1.4, install package."""
    def __init__(self, system):
        """ Initiliase the rat 6.1.4 package."""
        super(RAT614, self).__init__("rat-6.1.4", system, "root-5.34.36", "6.1.4")


class RAT613(ratreleases.RatRelease6):
    """ Rat release-6.1.3, install package."""
    def __init__(self, system):
        """ Initiliase the rat 6.1.3 package."""
        super(RAT613, self).__init__("rat-6.1.3", system, "root-5.34.36", "6.1.3")


class RAT612(ratreleases.RatRelease6):
    """ Rat release-6.1.2, install package."""
    def __init__(self, system):
        """ Initiliase the rat 6.1.2 package."""
        super(RAT612, self).__init__("rat-6.1.2", system, "root-5.34.36", "6.1.2")


class RAT611(ratreleases.RatRelease6):
    """ Rat release-6.1.1, install package."""
    def __init__(self, system):
        """ Initiliase the rat 6.1.1 package."""
        super(RAT611, self).__init__("rat-6.1.1", system, "root-5.34.36", "6.1.1")


class RAT610(ratreleases.RatRelease6):
    """ Rat release-6.1.0, install package."""
    def __init__(self, system):
        """ Initiliase the rat 6.1.0 package."""
        super(RAT610, self).__init__("rat-6.1.0", system, "root-5.34.34", "6.1.0")


class RAT601(ratreleases.RatRelease6):
    """ Rat release-6.0.1, install package."""
    def __init__(self, system):
        """ Initiliase the rat 6.0.1 package."""
        super(RAT601, self).__init__("rat-6.0.1", system, "root-5.34.34", "6.0.1", postgres=True)


class RAT600(ratreleases.RatRelease6):
    """ Rat release-6.0.0, install package."""
    def __init__(self, system):
        """ Initiliase the rat 6.0.0 package."""
        super(RAT600, self).__init__("rat-6.0.0", system, "root-5.34.34", "RAT-6.0.0-alpha", postgres=True)


class RAT532(ratreleases.RatRelease5):
    """ Rat release-5.3.2, install package."""
    def __init__(self, system):
        """ Initiliase the rat 5.3.2 package."""
        super(RAT532, self).__init__("rat-5.3.2", system, "root-5.34.34", "RAT-5.3.2-water_prod")


class RAT531(ratreleases.RatRelease5):
    """ Rat release-5.3.1, install package."""
    def __init__(self, system):
        """ Initiliase the rat 5.3.1 package."""
        super(RAT531, self).__init__("rat-5.3.1", system, "root-5.34.30", "5.3.1")


class RAT530(ratreleases.RatRelease5):
    """ Rat release-5.3.0, install package."""
    def __init__(self, system):
        """ Initiliase the rat 5.3.0 package."""
        super(RAT530, self).__init__("rat-5.3.0", system, "root-5.34.30", "5.3.0")


class RAT523(ratreleases.RatRelease5):
    """ Rat release-5.2.3, install package."""
    def __init__(self, system):
        """ Initiliase the rat 5.2.3 package."""
        super(RAT523, self).__init__("rat-5.2.3", system, "root-5.34.30", "5.2.3")


class RAT522(ratreleases.RatRelease5):
    """ Rat release-5.2.2, install package."""
    def __init__(self, system):
        """ Initiliase the rat 5.2.2 package."""
        super(RAT522, self).__init__("rat-5.2.2", system, "root-5.34.30", "5.2.2")


class RAT521(ratreleases.RatRelease5):
    """ Rat release-5.2.1, install package."""
    def __init__(self, system):
        """ Initiliase the rat 5.2.1 package."""
        super(RAT521, self).__init__("rat-5.2.1", system, "root-5.34.30", "5.2.1")


class RAT520(ratreleases.RatRelease5):
    """ Rat release-5.2.0, install package."""
    def __init__(self, system):
        """ Initiliase the rat 5.2.0 package."""
        super(RAT520, self).__init__("rat-5.2.0", system, "root-5.34.30", "5.2.0")


class RAT510(ratreleases.RatRelease5):
    """ Rat release-5.1.0, install package."""
    def __init__(self, system):
        """ Initiliase the rat 5.1.0 package."""
        super(RAT510, self).__init__("rat-5.1.0", system, "root-5.34.30", "5.1.0")


class RAT503(ratreleases.RatRelease5):
    """ Rat release-5.0.3, install package."""
    def __init__(self, system):
        """ Initiliase the rat 5.0.3 package."""
        super(RAT503, self).__init__("rat-5.0.3", system, "root-5.34.30", "5.0.3")


class RAT502(ratreleases.RatRelease5):
    """ Rat release-5.0.2, install package."""
    def __init__(self, system):
        """ Initiliase the rat 5.0.2 package."""
        super(RAT502, self).__init__("rat-5.0.2", system, "root-5.34.30", "5.0.2")


class RAT501(ratreleases.RatRelease5):
    """ Rat release-5.0.1, install package."""
    def __init__(self, system):
        """ Initiliase the rat 5.0.1 package."""
        super(RAT501, self).__init__("rat-5.0.1", system, "root-5.34.30", "5.0.1")


class RAT50(ratreleases.RatRelease5):
    """ Rat release-5.0.0, install package."""
    def __init__(self, system):
        """ Initiliase the rat 5.0.0 package."""
        super(RAT50, self).__init__("rat-5.0.0", system, "root-5.34.30", "5.0.0")


class RAT46(ratreleases.RatRelease4Post4):
    """ Rat release-4.6.0, install package."""
    def __init__(self, system):
        """ Initiliase the rat 4.6.0 package."""
        super(RAT46, self).__init__("rat-4.6.0", system, "root-5.34.18", "4.6.0")


class RAT45(ratreleases.RatRelease4Post4):
    """ Rat release-4.5.0, install package."""
    def __init__(self, system):
        """ Initiliase the rat 4.5.0 package."""
        super(RAT45, self).__init__("rat-4.5.0", system, "root-5.34.11", "4.5.0")


class RAT44(ratreleases.RatRelease4Post1):
    """ Rat release-4.4.0, install package."""
    def __init__(self, system):
        """ Initiliase the rat 4.4.0 package."""
        super(RAT44, self).__init__("rat-4.4.0", system, "root-5.34.08", "4.4.0")


class RAT43(ratreleases.RatRelease4Post1):
    """ Rat release-4.3.0, install package."""
    def __init__(self, system):
        """ Initiliase the rat 4.3.0 package."""
        super(RAT43, self).__init__("rat-4.3.0", system, "root-5.34.08", "release-4.3.0")


class RAT42(ratreleases.RatRelease4Post1):
    """ Rat release-4.20, install package."""
    def __init__(self, system):
        """ Initiliase the rat 4.2 package."""
        super(RAT42, self).__init__("rat-4.2", system, "root-5.34.02", "release-4.20")


class RAT421(ratreleases.RatRelease4Post1):
    """ Rat release-4.2.1, install package."""
    def __init__(self, system):
        """ Initiliase the rat 4.2.1 package."""
        super(RAT421, self).__init__("rat-4.2.1", system, "root-5.34.02", "release-4.2.1")


class RAT41(ratreleases.RatRelease4Pre2):
    """ Rat release-4.10, install package."""
    def __init__(self, system):
        """ Initiliase the rat 4.1 package."""
        super(RAT41, self).__init__("rat-4.1", system, "root-5.34.02", "release-4.10")


class RAT4(ratreleases.RatRelease4Pre2):
    """ Rat release-4.00, install package."""
    def __init__(self, system):
        """ Initiliase the rat 4.0 package."""
        super(RAT4, self).__init__("rat-4", system, "root-5.32.04", "release-4.00")


class RAT3(ratreleases.RatRelease3):
    """ Rat release-3.00, install package."""
    def __init__(self, system):
        """ Initiliase the rat 3.0 package."""
        super(RAT3, self).__init__("rat-3", system, "release-3.00")


class RAT2(ratreleases.RatRelease2):
    """ Rat release-2.00, install package."""
    def __init__(self, system):
        """ Initiliase the rat 2.0 package."""
        super(RAT2, self).__init__("rat-2", system, "release-2.00")


class RAT1(ratreleases.RatRelease0and1):
    """ Rat release-1.00, install package."""
    def __init__(self, system):
        """ Initiliase the rat 1.0 package."""
        super(RAT1, self).__init__("rat-1", system, "release-1.00")


class RAT0(ratreleases.RatRelease0and1):
    """ Rat release-0.00, install package."""
    def __init__(self, system):
        """ Initiliase the rat 0.0 package."""
        super(RAT0, self).__init__("rat-0", system, "release-0.00")

