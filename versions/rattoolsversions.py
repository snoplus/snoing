#!/usr/bin/env python
#
# RatToolsDev
#
# The development versions of rattools 
#
# Author P G Jones - 15/10/2012 <p.g.jones@qmul.ac.uk> : First revision
####################################################################################################
import rattools

class RatToolsDev(rattools.RatTools):
    def __init__(self, system):
        """ Initialise dev version."""
        super(RatToolsDev, self).__init__("rattools-dev", system, "root-5.32.04")
