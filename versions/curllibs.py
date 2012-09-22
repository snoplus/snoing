#!/usr/bin/env python
#
# Uuid
#
# The Curl prerequisites
#
# Author P G Jones - 23/06/2012 <p.g.jones@qmul.ac.uk> : First revision
# Author P G Jones - 22/09/2012 <p.g.jones@qmul.ac.uk> : Major refactor of snoing.
####################################################################################################

import librarypackage

class Uuid(librarypackage.LibraryPackage):
    """ Package for the universal ids, needed by curl development library."""
    def __init__(self, system):
        super(Uuid, self).__init__("uuid", system, "Install uuid-dev on this system.", "uuid", "uuid/uuid.h")
