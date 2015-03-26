#!/usr/bin/env python
#
# XercesC
#
# The xercesc package installer
#
# Author P G Jones - 19/05/2012 <p.g.jones@qmul.ac.uk> : First revision
# Author P G Jones - 22/09/2012 <p.g.jones@qmul.ac.uk> : Major refactor of snoing.
####################################################################################################
import conditionallibrarypackage
import os

class XercesC(conditionallibrarypackage.ConditionalLibraryPackage):
    """ XercesC install package."""
    def __init__(self, name, system, tar_name):
        """ Initlaise the XercesC packages."""
        super(XercesC, self).__init__(name, system, "xerces-c")
        self._tar_name = tar_name
    def get_dependencies(self):
        """ Return the dependencies."""
        return ["curl-7.26.0"]
    def _is_downloaded(self):
        """ Check if the tar ball has been downloaded."""
        return self._system.file_exists(self._tar_name)
    def _is_installed(self):
        """ Check if xercesc installed."""
        return self._system.library_exists("libxerces-c", os.path.join(self.get_install_path(), "lib"))
    def _download(self):
        """ Download the 3.1.x version."""
        download_name = "http://archive.apache.org/dist/xerces/c/3/sources/" + self._tar_name
        print download_name
        self._system.download_file("http://archive.apache.org/dist/xerces/c/3/sources/" + self._tar_name)        
    def _install(self):
        """ Install the 3.1.x version."""
        source_path = os.path.join(self._system.get_install_path(), "%s-source" % self._name)
        self._system.untar_file(self._tar_name, source_path, 1)
        self._system.execute_command("./configure", cwd=source_path)
        self._system.execute_command("make", cwd=source_path)
        self._system.execute_command("make", ["install", "prefix=%s" % self.get_install_path()], 
                                     cwd=source_path)
