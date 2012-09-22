#!/usr/bin/env python
#
# XercesC311
#
# The xercesc release versions
#
# Author P G Jones - 19/05/2012 <p.g.jones@qmul.ac.uk> : First revision
# Author P G Jones - 22/09/2012 <p.g.jones@qmul.ac.uk> : Major refactor of snoing.
####################################################################################################
import xercesc

class XercesC311(xercesc.XercesC):
    """ XercesC 3.1.1 version."""
    def __init__(self, system):
        super(XercesC311, self).__init__("xerces-c-3.1.1", system, "xerces-c-3.1.1.tar.gz")
