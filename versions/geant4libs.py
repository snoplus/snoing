#!/usr/bin/env python
#
# Xt, Xmu, Xi, Expat
#
# Libraries required by geant4
#
# Author P G Jones - 22/06/2012 <p.g.jones@qmul.ac.uk> : First revision
# Author P G Jones - 22/09/2012 <p.g.jones@qmul.ac.uk> : Major refactor of snoing.
# Author K E Gilje - 05/09/2018 <gilje@ualberta.ca> : Including Expat library check
####################################################################################################

import librarypackage

class Expat(librarypackage.LibraryPackage):
    """Package for the Expat library."""
    def __init__(self, system):
        super(Expat, self).__init__('expat', system, 'Install expat-devel on this system.', 'expat',
                                    ['expat.h'])

class Xt(librarypackage.LibraryPackage):
    """Package for the Xt library."""
    def __init__(self, system):
        super(Xt, self).__init__('Xt', system, 'Install libXt-devel on this system.', 'Xt',
                                 ['X11/Intrinsic.h'])


class Xmu(librarypackage.LibraryPackage):
    """Package for the Xmu library."""
    def __init__(self, system):
        super(Xmu, self).__init__('Xmu', system, 'Install Xmu-devel on this system.', 'Xmu',
                                  ['X11/Xmu/Xmu.h'])


class Xi(librarypackage.LibraryPackage):
    """Package for the Xi library. """
    def __init__(self, system):
        super(Xi, self).__init__('Xi', system, 'Install Xi-devel on this system.', 'Xi',
                                 ['X11/extensions/XI.h'])
