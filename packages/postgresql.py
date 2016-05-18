#!/usr/bin/env python
#
# PostgreSQL
#
# PostgreSQL package installer.
#
# Author M Mottram - 06/06/2016  <m.mottram@qmul.ac.uk> : First revision
#######################################################################
import conditionallibrarypackage
import os
import stat
import shutil
from distutils.version import LooseVersion

class PostgreSQL(conditionallibrarypackage.ConditionalLibraryPackage):
    """ Base PostgreSQL installer."""

    def __init__(self, name, system, version):
        """ Initialise the PostgreSQL package."""
        super(PostgreSQL, self).__init__(name, system, "pq", [])
        self._version = version

    def get_tar_name(self):
        """ Return the tarball name"""
        return "postgresql-%s.tar.gz" % self._version

    # Functions to override
    def get_dependencies(self):
        """ Return the dependency names as a list of names."""
        return ["make", "g++", "gcc"]

    def _is_downloaded(self):
        """ Check the tarball has been downloaded"""
        return self._system.file_exists(self.get_tar_name())

    def _is_system_installed( self ):
        """ Override to ensure version is correct"""
        installed = super(PostgreSQL, self)._is_system_installed()
        if installed:
            try:
                output = self._system.execute_command('pg_config', ['--version'])
            except:
                installed = False
            else:
                version = output.split()[1]
                if LooseVersion(version) < LooseVersion(self._version):
                    installed = False
        return installed

    def _is_installed(self):
        """ Check both binaries and libraries are installed"""
        binaries = self._system.file_exists("pg_config", os.path.join(self.get_install_path(), "bin"))
        libraries = (self._system.file_exists("libpq.so", os.path.join(self.get_install_path(), "lib")) or \
                         self._system.file_exists("libpq.dylib", os.path.join(self.get_install_path(), "lib")))
        return binaries and libraries

    def _download(self):
        """ Download PostgreSQL"""
        self._system.download_file("https://ftp.postgresql.org/pub/source/v%s/%s" %
                                   (self._version, self.get_tar_name()))

    def _install(self):
        """ Just install the client libraries"""
        source_path = os.path.join(self._system.get_install_path(), "%s-source" % self._name)
        self._system.untar_file(self.get_tar_name(), source_path, 1)
        self._system.configure_command(args=["prefix=%s" % self.get_install_path()], cwd=source_path)
        self._system.execute_command("make", [], source_path)
        self._system.execute_command("make", ["-C", "src/bin", "install"], source_path)
        self._system.execute_command("make", ["-C", "src/include", "install"], source_path)
        self._system.execute_command("make", ["-C", "src/interfaces", "install"], source_path)
        self._system.execute_command("make", ["-C", "doc", "install"], source_path)
        shutil.rmtree(source_path)
