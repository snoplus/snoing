#!/usr/bin/env python
#
# Cmake288
#
# The cmake release versions
#
# Author P G Jones - 24/09/2012 <p.g.jones@qmul.ac.uk> : First revision
####################################################################################################
import cmake

class Cmake288(cmake.Cmake):
    """ Cmake 2.8.8, install package."""
    def __init__(self, system):
        """ Initiliase the cmake 2.8.8 package."""
        super(Cmake288, self).__init__("cmake", system, "cmake-2.8.8.tar.gz")
    def _download(self):
        """ Download the 2.8 version."""
        self._system.download_file("http://www.cmake.org/files/v2.8/" + self._tar_name)
