#!/usr/bin/env python
# Author O Wasalski - 13/06/2012 <wasalski@berkeley.edu> : First revision
# The bzip2 conditional package
import os
import PackageUtil
import ConditionalLibraryPackage

class Bzip2(ConditionalLibraryPackage.ConditionalLibraryPackage):
    """ bzip2 install package."""

    def __init__(self):
        """ Initialize the bzip2 package."""
        super(Bzip2, self).__init__("bzip2-1.0.6", "bz2", "bzlib.h")
        installPath = os.path.join( PackageUtil.kInstallPath, self._Name )
        self._TarName = self._Name + ".tar.gz"

        files = [os.path.join("bin", "bzip2"),
                 os.path.join("lib", "lib%s.a" %self._Library),
                 os.path.join("include", self._Header)]
        self._Files = [os.path.join(installPath, f) for f in files]
        return

    def _CheckState(self):
        """ Check if downloaded and installed."""
        if os.path.isfile(os.path.join(PackageUtil.kCachePath, self._TarName )):
            self._SetMode(1) # Downloaded
        if all([os.path.isfile(f) for f in self._Files]):
            self._SetMode( 2 ) # Installed as well
        return

    def _Download(self):
        url = "http://www.bzip.org/1.0.6/" + self._TarName
        return PackageUtil.DownloadFile(url)

    def _Install(self):
        installPath = self.GetInstallPath()
        PackageUtil.UnTarFile(self._TarName, self.GetInstallPath(), 1)
        PackageUtil.ExecuteSimpleCommand("make", ["-f", "Makefile-libbz2_so"], 
                                         None, installPath)
        args = ["install", "PREFIX=" + installPath]
        return PackageUtil.ExecuteSimpleCommand("make", args, None, installPath)
