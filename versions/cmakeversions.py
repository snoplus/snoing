#!/usr/bin/env python
#
# Cmake288
#
# The cmake release versions
#
# Author P G Jones - 24/09/2012 <p.g.jones@qmul.ac.uk> : First revision
####################################################################################################
import cmake

class Cmake3143(cmake.Cmake):
    """ Cmake 3.14.3, install package."""
    def __init__(self, system):
        """ Initiliase the cmake 3.14.3 package."""
        super(Cmake3143, self).__init__("cmake-3.14.3", system, "cmake-3.14.3.tar.gz")
    def _download(self):
        """ Download the 3.14.3 version."""
        self._system.download_file("http://www.cmake.org/files/v3.14/" + self._tar_name)

class Cmake2812(cmake.Cmake):
    """ Cmake 2.8.12, install package."""
    def __init__(self, system):
        """ Initiliase the cmake 2.8.12.1 package."""
        super(Cmake2812, self).__init__("cmake-2.8.12", system, "cmake-2.8.12.1.tar.gz")
    def _download(self):
        """ Download the 2.8 version."""
        self._system.download_file("http://www.cmake.org/files/v2.8/" + self._tar_name)

class Cmake288(cmake.Cmake):
    """ Cmake 2.8.8, install package."""
    def __init__(self, system):
        """ Initiliase the cmake 2.8.8 package."""
        super(Cmake288, self).__init__("cmake-2.8.8", system, "cmake-2.8.8.tar.gz")
    def _download(self):
        """ Download the 2.8 version."""
        self._system.download_file("http://www.cmake.org/files/v2.8/" + self._tar_name)
