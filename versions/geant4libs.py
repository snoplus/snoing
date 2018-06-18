#!/usr/bin/env python
#
# Xt, Xmu, Xi
#
# Libraries required by geant4
#
# Author P G Jones - 22/06/2012 <p.g.jones@qmul.ac.uk> : First revision
# Author P G Jones - 22/09/2012 <p.g.jones@qmul.ac.uk> : Major refactor of snoing.
####################################################################################################

import librarypackage


class Xt(librarypackage.LibraryPackage):
    """Package for the Xt library."""
    def __init__(self, system):
        super(Xt, self).__init__('Xt', system, 'Install Xt-dev on this system.', 'Xt',
                                 ['X11/Intrinsic.h'])


class Xmu(librarypackage.LibraryPackage):
    """Package for the Xmu library."""
    def __init__(self, system):
        super(Xmu, self).__init__('Xmu', system, 'Install Xmu-dev on this system.', 'Xmu',
                                  ['X11/Xmu/Xmu.h'])


class Xi(librarypackage.LibraryPackage):
    """Package for the Xi library. """
    def __init__(self, system):
        super(Xi, self).__init__('Xi', system, 'Install Xi-dev on this system.', 'Xi',
                                 ['X11/extensions/XI.h'])
