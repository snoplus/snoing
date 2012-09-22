#!/usr/bin/env python
#
# Sfml
#
# The sfml installer.
#
# Author O Wasalski - 07/06/2012 <wasalski@berkeley.edu> : First revision, new file
# Author P G Jones - 23/06/2012 <p.g.jones@qmul.ac.uk> : Refactor of Package Structure 
# Author P G Jones - 22/09/2012 <p.g.jones@qmul.ac.uk> : Major refactor of snoing.
####################################################################################################
import localpackage
import installmode
import os

class Sfml(localpackage.LocalPackage):
    """ Base sfml installer package."""
    def __init__(self, name, system, tar_name):
        """ Initialise sfml with the tar_name."""
        super(Sfml, self).__init__(name, system)
        self._tar_name = tar_name
        self.set_install_mode(installmode.Graphical)
    def get_dependencies(self):
        """ Return the required dependencies."""
        return ["cmake", "pthread", "opengl", "xlib", "xrandr", "freetype", "glew", "jpeg", 
                "sndfile", "openal"]
    def _is_downloaded(self):
        """ Has the tar file been downloaded."""
        return self._system.file_exists(self._tar_name)
    def _is_installed(self):
        """ Has sfml been installed."""
        lib_dir = os.path.join(self.get_install_path(), "lib")
        libs = ["audio", "graphics", "network", "system", "window"]
        installed = True
        for lib in libs:
            installed = installed and self._system.library_exists("libsfml-%s" % lib, lib_dir)
        return installed
    def _download(self):
        """ Download the tar file."""
        self._download_pipe += self._system.download_file(
            "https://github.com/LaurentGomila/SFML/tarball/" + self._tar_name)
    def _install(self):
        """ Install sfml."""
        self._system.untar_file(self._tar_name, self.get_install_path(), 1)
        cmake_command = "cmake"
        if self._dependency_paths["cmake"] is not None: # Special cmake installed
            cmake_command = "%s/bin/cmake" % self._dependency_paths["cmake"]
        self._install_pipe += self._system.execute_command(cmake_command, 
                                                           ["-DCMAKE_INSTALL_PREFIX:PATH=$PWD"], 
                                                           cwd=self.get_install_path())
        self._install_pipe += self._system.execute_command("make", cwd=self.get_install_path())
