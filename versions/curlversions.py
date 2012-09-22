#!/usr/bin/env python
#
# Curl7260
#
# Curl releases
#
# Author O Wasalski - 05/06/2012 <wasalski@berkeley.edu> : First revision, new file.
# Author P G Jones - 22/09/2012 <p.g.jones@qmul.ac.uk> : Major refactor of snoing.
####################################################################################################
import curl

class Curl7260(curl.Curl):
    """ Package for curl. """
    def __init__(self, system):
        """ Initialize the package, set the name."""
        super(Curl7260, self).__init__("curl-7.26.0", system, "curl-7.26.0.tar.gz")


    
