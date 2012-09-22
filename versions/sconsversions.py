#!/usr/bin/env python
#
# SCONS210, SCONS120
#
# The scons release versions
# 
# Author P G Jones - 13/05/2012 <p.g.jones@qmul.ac.uk> : First revision
# Author P G Jones - 22/09/2012 <p.g.jones@qmul.ac.uk> : Major refactor of snoing.
####################################################################################################
import scons

class SCONS210(scons.Scons):
    """ Scons 2.1.0, install package."""
    def __init__(self, system):
        """ Initiliase the scons 2.1.0 package."""
        super(SCONS210, self).__init__("scons-2.1.0", system, "scons-2.1.0.tar.gz")
    def _download(self):
        """ Derived classes should override this to download the package."""
        self._download_pipe += self._system.download_file(
            "http://downloads.sourceforge.net/project/scons/scons/2.1.0/scons-2.1.0.tar.gz")

class SCONS120(Scons.Scons):
    """ Scons 1.2.0, install package."""
    def __init__(self, system):
        """ Initiliase the scons 1.2.0 package."""
        super(SCONS120, self).__init__("scons-1.2.0", system, "scons-1.2.0.tar.gz")
    def _download(self):
        """ Derived classes should override this to download the package."""
        self._dowload_pipe += self._system.download_file(
            "http://downloads.sourceforge.net/project/scons/scons/1.2.0/scons-1.2.0.tar.gz")
