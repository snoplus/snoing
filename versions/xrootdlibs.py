#!/usr/bin/env python
#
# OpenSSLDev
#
# Required xrootd libraries.
#
# Author M Mottram - 19/04/2016 <m.mottram@qmul.ac.uk> : First revision
######################################################################################
import systempackage

class OpenSSLDev(systempackage.SystemPackage):
    """ Package for the openssl libraries."""

    def __init__(self, system):
        """ Initialise the package, set the name."""
        super(OpenSSLDev, self).__init__("openssl-dev", system, 
                                  "Install a openssl-dev compiler on this system")

    def check_state(self):
        """ Check the openssl-dev install state."""
        self._installed = self._system._test_compile(["openssl/opensslconf.h"])
