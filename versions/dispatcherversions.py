#!/usr/bin/env python
#
# DispatcherDev
#
# The development and release versions of dispatcher.
#
# Author K E Gilje - 06/09/2018 <gilje@ualberta.ca> : First revision
####################################################################################################
import dispatcher

class DispatcherDev(dispatcher.Dispatcher):
    def __init__(self, system):
        """ Initialise dev version."""
        super(DispatcherDev, self).__init__("disp", system)
