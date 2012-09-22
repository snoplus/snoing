#!/usr/bin/env python
#
# Scons
#
# Scons package installer.
#
# Author P G Jones - 12/05/2012 <p.g.jones@qmul.ac.uk> : First revision
# Author P G Jones - 22/09/2012 <p.g.jones@qmul.ac.uk> : Major refactor of snoing.
####################################################################################################
import localpackage
import os
import stat

class Scons(localpackage.LocalPackage):
    """ Base scons installer, different versions only have different names."""
    def __init__(self, name, system, tar_name):
        """ Initialise the scons package."""
        super(Scons, self).__init__(name, system)
        self._tar_name = tar_name
        return
    # Functions to override
    def get_dependencies(self):
        """ Return the dependency names as a list of names."""
        return ["python"]
    def _is_downloaded(self):
        """ Check the tar ball has been downloaded."""
        return self._system.file_exists(self._tar_name)
    def _is_installed(self):
        """ Check the script has been marked as executable."""
        return self._system.file_exists("scons", os.path.join(self.get_install_path(), "script")) and \
            bool(os.stat(os.path.join(self.get_install_path(), "script/scons")).st_mode & stat.S_IXUSR)
    def _install(self):
        """ Mark the script as executable."""
        self._install_pipe += self._system.untar_file(self._tar_name, self.get_install_path(), 1)
        os.chmod(os.path.join(self.get_install_path(), "script/scons"), 0755)
