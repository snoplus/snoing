#!/usr/bin/env python
#
# Bzip2
#
# The bzip2 conditional package, required for RATDB functions
#
# Author O Wasalski - 13/06/2012 <wasalski@berkeley.edu> : First revision, new file
# Author P G Jones - 23/06/2012 <p.g.jones@qmul.ac.uk> : Refactor of Package Structure 
# Author P G Jones - 22/09/2012 <p.g.jones@qmul.ac.uk> : Major refactor of snoing.
####################################################################################################
import conditionallibrarypackage
import os

class Bzip2(conditionallibrarypackage.ConditionalLibraryPackage):
    """ Base bzip2 installer package."""
    def __init__(self, name, system, tar_name):
        """ Initialise bzip2 with the tar_name."""
        super( Bzip2, self ).__init__(name, system, "bz2", "bzlib.h")
        self._tar_name = tar_name
    def get_dependencies(self):
        """ Return the required dependencies."""
        return []
    def _is_downloaded(self):
        """ Has the tar file been downloaded."""
        return self._system.file_exists(self._tar_name)
    def _is_installed(self):
        """ Has bzip2 been installed."""
        return self._system.file_exists("bzlib.h", os.path.join(self.get_install_path(), "include")) and \
            self._system.library_exists("bz2", os.path.join(self.get_install_path(), "lib"))
    def _download(self):
        """ Download the tar file."""
        self._download_pipe += self._system.download_file("http://www.bzip.org/1.0.6/" + self._tar_name)
    def _Install( self ):
        """ Install bzip2."""
        self._system.untar_file(self._tar_name, self.get_install_path(), 1)
        self._install_pipe += self._system.execute_command("make", ["-f", "Makefile-libbz2_so"], 
                                                           cwd=self.get_install_path())
        self._install_pipe += self._system.execute_command("make", 
                                                           ["install", "PREFIX=" + self.get_install_path()], 
                                                           cwd=self.get_install_path())
