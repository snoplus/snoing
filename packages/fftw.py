#!/usr/bin/env python
#
# fftw
#
# FFTW installer
#
# Author:
#  - 2015-06-05 M Mottram <m.mottram@qmul.ac.uk> first instance
####################################################################################################
import conditionallibrarypackage
import installmode
import os

class Fftw(conditionallibrarypackage.ConditionalLibraryPackage):
    """ Base fftw installer package. """
    def __init__(self, name, system, tar_name):
        super(Fftw, self).__init__(name, system, "fftw", ["fftw/fftw.h"])
        self._tar_name = tar_name
    def get_dependencies(self):
        """ Return the dependency names as a list of names."""
        return []
    def _is_downloaded(self):
        """ Check if package is downloaded."""
        return self._system.file_exists(self._tar_name)
    def _is_installed(self):
        """ Returns true if the header, library and config files are in the proper location."""
        header = self._system.file_exists("fftw3.h", os.path.join(self.get_install_path(), 
                                                                 "include"))
        lib = self._system.library_exists("libfftw3", os.path.join(self.get_install_path(), "lib"))
        return header and lib
    def _download(self):
        """ Downloads a fftw tarball from the fftw website."""
        self._system.download_file("http://www.fftw.org/" + self._tar_name)
    def _install(self):
        """ Install fftw."""
        source_path = os.path.join(self._system.get_install_path(), "%s-source" % self._name)
        self._system.untar_file(self._tar_name, source_path, 1)
        self._system.execute_command("./configure", cwd=source_path)
        self._system.execute_command("make", cwd=source_path)
        self._system.execute_command("make", ["install", "prefix=%s" % self.get_install_path()], cwd=source_path)
        if self._system.get_install_mode() == installmode.Grid:
            shutil.rmtree(source_path)
