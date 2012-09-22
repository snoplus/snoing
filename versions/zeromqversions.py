#!/usr/bin/env python
#
# Zeromq220
#
# The Zeromq versions
#
# Author P G Jones - 19/05/2012 <p.g.jones@qmul.ac.uk> : First revision
# Author P G Jones - 22/09/2012 <p.g.jones@qmul.ac.uk> : Major refactor of snoing.
####################################################################################################
import zeromq

class Zeromq220(zeromq.Zeromq):
    """ Zeromq220 install package."""
    def __init__(self, system):
        """ Initlaise the ZMQ packages."""
        super(Zeromq220, self).__init__("zeromq-2.2.0", system, "zeromq-2.2.0.tar.gz")
