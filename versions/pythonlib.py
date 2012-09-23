#!/usr/bin/env python
#
# Python, PythonDev, PythonDev24
#
# Checks for python and the development headers
#
# Author P G Jones - 11/07/2012 <p.g.jones@qmul.ac.uk> : First revision
# Author P G Jones - 22/09/2012 <p.g.jones@qmul.ac.uk> : Major refactor of snoing.
####################################################################################################
import commandpackage
import systempackage
import librarypackage

class Python(commandpackage.CommandPackage):
    """ Package for the python development library."""
    def __init__(self, system):
        super(Python, self).__init__("python", system, "Install python on this system, how on earth is this possible? snoing is written in python")

class PythonDev(systempackage.SystemPackage):
    """ Package for the python development library."""
    def __init__(self, system):
        super(PythonDev, self).__init__("python-dev", system, 
                                        "Install python dev(el) on this system.")
    def check_state(self):
        """ Check the python-dev install state."""
        # First check for python config
        if self._system.find_library("python-config") is not None:
            # Now can test for linking
            self._installed = self._system.test_config("python-config", ["Python.h"])

class PythonDev24(librarypackage.LibraryPackage):
    """ Package for python dev 2.4, default on Sl5, doesn't have python-config."""
    def __init__(self, system):
        super(PythonDev24, self).__init__("python-dev-2.4", system, 
                                          "Install python dev(el) on this system.", "python2.4")
