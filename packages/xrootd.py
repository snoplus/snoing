#!/usr/bin/env python
#
# XRootD
#
# XRootD package installer.
#
# Author M Mottram - 15/04/2016 <m.mottram@qmul.ac.uk> : First revision
#######################################################################
import localpackage
import os
import stat
import shutil

class XRootD(localpackage.LocalPackage):
    """ Base XRootD installer."""

    def __init__(self, name, system, version):
        """ Initialise the XRootD package."""
        super(XRootD, self).__init__(name, system)
        self._version = version

    def get_tar_name(self):
        """ Return the tarball name"""
        return "xrootd-%s.tar.gz" % self._version

    # Functions to override
    def get_dependencies(self):
        """ Return the dependency names as a list of names."""
        return ["openssl-dev", "cmake-2.8.12"]

    def _is_downloaded(self):
        """ Check the tarball has been downloaded"""
        return self._system.file_exists(self.get_tar_name())

    def _is_installed(self):
        """ Check the script has been marked as executable."""
        return self._system.file_exists("xrootd", os.path.join(self.get_install_path(), "bin")) and \
            bool(os.stat(os.path.join(self.get_install_path(), "bin/xrootd")).st_mode & stat.S_IXUSR)

    def _download(self):
        """ Download XRootD"""
        self._system.download_file("http://xrootd.org/download/v%s/%s" % (self._version,
                                                                          self.get_tar_name()))

    def _install(self):
        """ Mark the script as executable"""
        source_path = os.path.join(self._system.get_install_path(), "%s-source" % self._name)
        self._system.untar_file(self.get_tar_name(), source_path, 1)
        if not os.path.exists(self.get_install_path()):
            os.makedirs(self.get_install_path())
        cmake_opts = [source_path,
                      "-DCMAKE_INSTALL_PREFIX=%s" % self.get_install_path(),
                      "-DENABLE_PERL=FALSE"]
        cmake_command = "cmake"
        if self._dependency_paths["cmake-2.8.12"] is not None:
            cmake_command = "%s/bin/cmake" % self._dependency_paths["cmake-2.8.12"]
        self._system.configure_command(cmake_command, cmake_opts, self.get_install_path(),
                                       config_type="xrootd")
        self._system.execute_command("make", [], self.get_install_path())
        self._system.execute_command("make", ["install"], self.get_install_path())
        shutil.rmtree(source_path)
