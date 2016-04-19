#!/usr/bin/env python
#
# XRootD430
#
# The XRootD release versions
#
# Author M Mottram - 15/04/2016 <m.mottram@qmul.ac.uk> : First revision
####################################################################################################
import xrootd

class XRootD430(xrootd.XRootD):
    """ XRootD 4.3.0, install package"""

    def __init__(self, system):
        """Initialise the XRootD 4.3.0 package."""
        super(XRootD430, self).__init__("xrootd-4.3.0", system, "4.3.0")
