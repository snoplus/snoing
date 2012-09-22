#!/usr/bin/env python
#
# Sfml20RC, Sfml18
#
# The release versions of sfml. Version 1.8 is not an actual sfml release, but exists for bookeeping
# in snoing.
#
# Author O Wasalski - 07/06/2012 <wasalski@berkeley.edu> : First revision, new file.
# Author P G Jones - 24/06/2012 <p.g.jones@qmul.ac.uk> : Refactor for new package types.
# Author P G Jones - 22/09/2012 <p.g.jones@qmul.ac.uk> : Major refactor of snoing.
####################################################################################################
import sfml

class Sfml20RC(Sfml.Sfml):
    """ Installer for release 1.0 sfml-2.0 pre release version."""
    def __init__(self, system):
        """ Initialize the package, set the name."""
        super(Sfml20RC, self).__init__("sfml-2.0-rc", system, 
                                       "bdfc2dc3f538605d5e9d7a09a04f87b2a02d2b3f")

class Sfml18(Sfml.Sfml):
    """ Installer for air fill 1 & 2 sfml-2.0 pre release version."""
    def __init__(self, system):
        """ Initialize the package, set the name."""
        super(Sfml18, self).__init__("sfml-1.8", system, 
                                     "fa4415cf8a423e0ad3f1c0a84d053ca2d1eef134")
