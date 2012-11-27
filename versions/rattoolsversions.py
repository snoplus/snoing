#!/usr/bin/env python
#
# RatToolsDev
#
# The development versions of rattools 
#
# Author P G Jones - 15/10/2012 <p.g.jones@qmul.ac.uk> : First revision
####################################################################################################
import rattools

class RatToolsDev(rattools.RatToolsDevelopment):
    def __init__(self, system):
        """ Initialise dev version."""
        super(RatToolsDev, self).__init__("rattools-dev", system, "root-5.34.02")

class RatTools1(rattools.RatToolsRelease):
    def __init__(self, system):
        """ Initialise an arbitrary snaphot version."""
        super(RatTools1, self).__init__("rattools-1", system, "root-5.32.04", "rat-4",
                                        "ebd71f14121dee64f6d0f01b72730b29b075e6d6")
