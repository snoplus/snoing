#!/usr/bin/env python
#
# Bzip2106
#
# The bzip2 versions
#
# Author O Wasalski - 13/06/2012 <wasalski@berkeley.edu> : First revision
# Author P G Jones - 22/09/2012 <p.g.jones@qmul.ac.uk> : Major refactor of snoing.
####################################################################################################
import bzip2

class Bzip2106(bzip2.Bzip2):
    """ bzip2-1.0.6 install package."""
    def __init__(self, system):
        """ Initialize the bzip2 package."""
        super(Bzip2106, self).__init__("bzip2-1.0.6", system, "bzip2-1.0.6.tar.gz")
