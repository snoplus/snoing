#!/usr/bin/env python
#
# GollumGem
#
# The gollum release versions
#
# Author P G Jones - 29/09/2012 <p.g.jones@qmul.ac.uk> : First revision
####################################################################################################
import gollum

class GollumGem(gollum.Gollum):
    """ GollumGem, install package."""
    def __init__(self, system):
        """ Initiliase the gollum package."""
        super(GollumGem, self).__init__("gollum", system)
