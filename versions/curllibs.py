#!/usr/bin/env python
#
# Uuid
#
# The Curl prerequisites
#
# Author P G Jones - 23/06/2012 <p.g.jones@qmul.ac.uk> : First revision
# Author P G Jones - 22/09/2012 <p.g.jones@qmul.ac.uk> : Major refactor of snoing.
####################################################################################################
import systempackage
import librarypackage

class Uuid(librarypackage.LibraryPackage):
    """ Package for the universal ids, needed by curl development library."""
    def __init__(self, system):
        super(Uuid, self).__init__("uuid", system, "Install uuid-dev on this system.", "uuid", 
                                   ["uuid/uuid.h"])

class OsspUuid(systempackage.SystemPackage):
    """ Package for the ossp-uuid development library."""
    def __init__(self, system):
        super(OsspUuid, self).__init__("ossp-uuid", system,
                                        "Install uuid-dev on this system.")
    def check_state(self):
        """ Check the ossp-uuid install state."""
        # First check for uuid config
        if self._system.find_library("uuid-config") is not None:
            # Now can test for linking
            self._installed = self._system.test_config("uuid-config", ["uuid.h"])
