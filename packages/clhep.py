#!/usr/bin/env python
#
# Clhep
#
# The installer for clhep packages
#
# Author P G Jones - 12/05/2012 <p.g.jones@qmul.ac.uk> : First revision
# Author P G Jones - 22/09/2012 <p.g.jones@qmul.ac.uk> : Major refactor of snoing.
####################################################################################################
import localpackage
import os

class Clhep(localpackage.LocalPackage):
    """ Base clhep installer."""
    def __init__(self, name, system, tar_name):
        """ Initialise the clhep package."""
        super(Clhep, self).__init__(name, system)
        self._tar_name = tar_name
    def get_dependencies(self):
        """ Return the dependency names as a list of names."""
        return ["make", "g++", "gcc"]
    def _is_downloaded(self):
        """ Check if downloaded."""
        return self._system.file_exists(self._tar_name)
    def _is_installed(self):
        """ Check if installed."""
        return self._system.library_exists("libCLHEP", os.path.join(self.get_install_path(), "lib"))
    def _download(self):
        """ Derived classes should override this to download the package. Return True on success."""
        self._download_pipe += self._system.download_file( 
            "http://proj-clhep.web.cern.ch/proj-clhep/DISTRIBUTION/tarFiles/" + self._tar_name)
    def _install(self):
        """ Install clhep."""
        self._install_pipe += self._system.untar_file(self._tar_name, self.get_install_path(), 2)
        self._install_pipe += self._system.execute_command('./configure', 
                                                           ['--prefix=%s' % self.get_install_path()], 
                                                           cwd=self.get_install_path())
        self._install_pipe += self._system.execute_command('make', [], cwd=self.get_install_path())
        self._install_pipe += self._system.execute_command('make', ["install"], cwd=self.get_install_path())

class ClhepPost2110(Clhep):
    """ Base clhep installer for packages post 2.1.1.0."""
    def __init__(self, name, system, tar_name):
        """ Initialise clhep installer."""
        super(ClhepPost2110, self).__init__(name, system, tar_name)
    def get_dependencies(self):
        """ Return the dependency names as a list of names."""
        return ["cmake", "make", "g++", "gcc"]
    def _install(self):
        """ Install clhep, using cmake. First untar to a source directory then install to the right path"""
        source_path = self._system.build_path(os.path.join(self._system.get_install_path(), "%s-source" % \
                                                              self._name))
        self._system.untar_file(self._tar_name, source_path, 2)
        cmake_opts = ["-DCMAKE_INSTALL_PREFIX=%s" % self.get_install_path()]
        cmake_opts.extend([sourcePath])
        cmake_command = "cmake"
        if self._dependency_paths["cmake"] is not None: # Special cmake installed
            cmake_command = "%s/bin/cmake" % self._dependency_paths["cmake"]
        self._install_pipe += self._system.execute_command(cmake_command, cmake_opts, cwd=self.get_install_path())
        self._install_pipe += self._system.execute_command("make", cwd=self.get_install_path())
        self._install_pipe += self._system.execute_command("make", ['install'], cwd=self.get_install_path())
