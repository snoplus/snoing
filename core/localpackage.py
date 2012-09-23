#!/usr/bin/env python
#
# LocalPackage
#
# Base class for packages that can be installed by snoing.
#
# Author P G Jones - 12/05/2012 <p.g.jones@qmul.ac.uk> : First revision
# Author P G Jones - 23/06/2012 <p.g.jones@qmul.ac.uk> : Refactor of Package Structure
# Author P G Jones - 23/06/2012 <p.g.jones@qmul.ac.uk> : Major refactor of snoing.
####################################################################################################
import package
import os

class LocalPackage(package.Package):
    """ Base class for packages that can be installed."""
    Initial, Downloaded, Installed, Updated = range(4) # Package states

    def __init__(self, name, system):
        """ Initialise the package."""
        super(LocalPackage, self).__init__(name, system)
        self._state = LocalPackage.Initial
        self._dependency_paths = {} # Dictionary of dependencies and the installed path
        self._install_mode = None # Optional install mode requirement
        self._download_pipe = "" # Download loggin output
        self._install_pipe = "" # Installation logging output
        self._install_path = os.path.join(self._system.get_install_path(), self._name)
        return
    def set_install_mode(self, mode):
        """ Specify the install mode."""
        self._install_mode = mode
    def get_install_mode(self):
        """ Return the install mode specified."""
        return self._install_mode
    def set_dependency_paths(self, paths):
        """ Set the dependency path dictionary."""
        self._dependency_paths = paths
    # State functions
    def _set_state(self, state):
        """ Set the current package state."""
        self._state = state
    def is_downloaded(self):
        """ Return package is downloaded."""
        return self._state >= LocalPackage.Downloaded
    def is_installed(self):
        """ Check and return if package is installed."""
        return self._state >= LocalPackage.Installed
    def is_updated(self):
        """ No way of checking, only updated if mode is 3."""
        return self._state >= LocalPackage.Updated
    # Overhead methods, mostly do checking then call the related _XXX functions
    def check_state(self):
        """ Check if the package is downloaded and/or installed."""
        if self._is_downloaded():
            self._set_state(LocalPackage.Downloaded)
        if self._is_installed():
            self._set_state(LocalPackage.Installed)
    def install(self):
        """ Full install process."""
        self.check_state() # Check the state first, saves effort
        self.download()
        if self.is_installed(): # Already installed, don't try again
            return 
        # Try installation, will raise exception if fails
        self._install()
        self._set_state(Installed)
    def download(self):
        """ Full download process."""
        self.check_state() # Check the state first, saves effort
        if self.is_downloaded(): # Already downloaded, don't try again
            return
        self._download()
        self._set_state(Downloaded)
    def update(self):
        """ Update the package install, usually deletes and reinstalls..."""
        self.check_state()
        if not self.is_installed(): # Not installed, no update rather just install
            self.install()
        else:
            self._update()
        self._set_satte(Updated)
    def remove(self):
        """ Default is to delete the directory, derived classes should add extra."""
        self._system.remove(self.get_install_path())
        self._remove() # Extra package specific stuff to remove
    # Functions to override
    def _update(self):
        """ Derived classes can overide this such that no deletion is carried out."""
        self.remove()
        self.install()
    def _remove(self):
        """ Derived classes can remove extra files via this."""
        pass
    # Functions to implement
    def get_dependencies(self):
        """ Return the dependency names as a list of names."""
        pass
    def _is_downloaded(self):
        """ Check if package is downloaded."""
        return False
    def _is_installed(self):
        """ Check if package is installed."""
        return False
    def _download(self):
        """ Derived classes should override this to download the package.."""
        pass
    def _install(self):
        """ Derived classes should override this to install the package, should install only when finished."""
        pass
