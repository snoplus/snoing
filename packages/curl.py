#!/usr/bin/env python
#
# Curl
#
# The curl installer
#
# Author O. Wasalski - 04/06/2012 <wasalski@berkeley.edu> : First revision, new file
# Author P G Jones - 23/06/2012 <p.g.jones@qmul.ac.uk> : Refactor of Package Structure
# Author P G Jones - 22/09/2012 <p.g.jones@qmul.ac.uk> : Major refactor of snoing.
####################################################################################################
import conditionallibrarypackage
import installmode
import os
import shutil

class Curl(conditionallibrarypackage.ConditionalLibraryPackage):
    """ Base curl installer package. """
    def __init__(self, name, system, tar_name):
        super(Curl, self).__init__(name, system, "curl", ["curl/curl.h"])
        self._tar_name = tar_name
    def get_dependencies(self):
        """ Return the dependency names as a list of names."""
        return [["uuid", "ossp-uuid"]]
    def _is_downloaded(self):
        """ Check if package is downloaded."""
        return self._system.file_exists(self._tar_name)
    def _is_installed(self):
        """ Returns true if the header, library and config files are in the proper location."""
        header = self._system.file_exists("curl.h", os.path.join(self.get_install_path(), 
                                                                 "include/curl"))
        lib = self._system.library_exists("libcurl", os.path.join(self.get_install_path(), "lib"))
        config = self._system.file_exists("curl-config", os.path.join(self.get_install_path(), "bin"))
        return header and lib and config
    def _download(self):
        """ Downloads a curl tarball from the curl website."""
        self._system.download_file("http://curl.haxx.se/download/" + self._tar_name)
    def _install(self):
        """ Install curl."""
        source_path = os.path.join(self._system.get_install_path(), "%s-source" % self._name)
        self._system.untar_file(self._tar_name, source_path, 1)
        self._system.configure_command(args=["--prefix=%s" % self.get_install_path()], 
                                       cwd=source_path, config_type="curl")
        self._system.execute_command("make", cwd=source_path)
        self._system.execute_command("make", ["install"], cwd=source_path)
        if self._system.get_install_mode() == installmode.Grid:
            shutil.rmtree(source_path)
