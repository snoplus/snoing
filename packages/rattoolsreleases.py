#!/usr/bin/env python
#
# RatToolsRelease1
#
# Base classes for the various rat-tools releases
#
#      M Mottram - 20/10/2012 <m.mottram@sussex.ac.uk>: First revision
####################################################################################################
import os
import rattools

class RatToolsRelease1(rattools.RatToolsRelease):
    """ Base package installer for rat-tools release 1 (just an arbitrary snapshot for now)."""
    def __init__(self, name, system, tar_name):
        """ Initlaise, take extra dependencies."""
        super(RatToolsRelease1, self).__init__(name, system, "root-5.32.04", "rat-4", tar_name)
