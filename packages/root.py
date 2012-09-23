#!/usr/bin/env python
#
# Root
#
# The root package installers
#
# Author P G Jones - 12/05/2012 <p.g.jones@qmul.ac.uk> : First revision
# Author P G Jones - 13/05/2012 <p.g.jones@qmul.ac.uk> : Added 5.32, 5.28, 5.24 versions (rat v3, v2, v1)
#        O Wasalski - 13/06/2012 <wasalski@berkeley.edu> : Building python module
# Author P G Jones - 22/09/2012 <p.g.jones@qmul.ac.uk> : Major refactor of snoing.
####################################################################################################
import localpackage
import installmode
import os

class Root(localpackage.LocalPackage):
    """ Base root installer, different versions only have different names."""
    def __init__(self, name, system, tar_name):
        """ Initialise the root package."""
        super(Root, self).__init__(name, system)
        self._tar_name = tar_name
    def get_dependencies(self):
        """ Return the dependency names as a list of names."""
        if self._system.get_install_mode() == installmode.Grid:
            return ["make", "g++", "gcc", "ld", "python", ["python-dev", "python-dev-2.4"]]
        else:
            return ["make", "g++", "gcc", "ld", "X11", "Xpm", "Xft", "Xext", "python", 
                    ["python-dev", "python-dev-2.4"]]
    def _is_downloaded(self):
        """ Check the tar ball has been downloaded."""
        return self._system.file_exists(self._tar_name)
    def _is_installed(self):
        """ Check if root is installed."""
        if self._system.get_install_mode() == installmode.Grid: #no X11, no bit/root
            return self._system.file_exists("root.exe", os.path.join(self.get_install_path(), "bin"))
        else:
            return os.path.exists(os.path.join(self.get_install_path(), "bin/root"))
    def _download(self):
        """ Download from cern."""
        self._download_pipe += self._system.download_file("ftp://root.cern.ch/root/" + self._tar_name)
    def _install(self):
        """ Install root."""
        self._install_pipe += PackageUtil.UnTarFile(self._tar_name, self.GetInstallPath(), 1)
        if self._system.get_os_type == system.Mac and os.path.exists('/usr/X11/lib'):
            args = ['--enable-minuit2', '--enable-roofit',  '--enable-python', 
                    '--with-x11-libdir=/usr/X11/lib','--with-xft-libdir=/usr/X11/lib',
                    '--with-xext-libdir=/usr/X11/lib']
        elif self._system.get_install_mode() == installmode.Grid:
            args = ['--enable-minuit2', '--enable-roofit',  '--enable-python', 
                    '--disable-castor', '--disable-rfio', '--disable-x11']
        else:
            args = ['--enable-minuit2', '--enable-roofit',  '--enable-python']
        self._install_pipe += self._system.configure_command( args=args, cwd=self.get_install_path())
        self._install_pipe += self._system.execute_command('make', cwd=self.get_install_path())
