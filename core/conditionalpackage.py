#!/usr/bin/env python
#
# ConditionalPackage
# 
# Checks if the package is already installed on the system, and if not it allows installation
#
# Author P G Jones - 19/05/2012 <p.g.jones@qmul.ac.uk> : First revision
# Author P G Jones - 23/06/2012 <p.g.jones@qmul.ac.uk> : Refactor of Package Structure
# Author P G Jones - 23/06/2012 <p.g.jones@qmul.ac.uk> : Major refactor of snoing.
####################################################################################################
import localpackage
import os

class ConditionalPackage(localpackage.LocalPackage):
    """ Base class to install libraries."""
    def __init__(self, name, system):
        """ Initialise the package."""
        super(ConditionalPackage, self).__init__(name, system)
        self._install_path = None # Override install path to be None unless locally installed.
        return
    def check_state( self ):
        """ Override the LocalPackage check_state to check if package is system wide installed, if 
        not check download and install state.
        """
        if self._is_system_installed():
            self._set_state(localpackage.LocalPackage.Installed)
        else: # Not on the system, set the install path and check the local state
            self._install_path = os.path.join(system.get_install_path(), self._name)
            super(ConditionalPackage, self).check_state()
        return        
    def update( self ):
        """ Override the LocalPackage update to check if the package is system wide installed, if
        not then consider updating.
        """
        if self._is_system_installed():
            self._set_state(localpackage.LocalPackage.Updated)
            return
        else: # Not on the system, set the install path and update
            self._install_path = os.path.join(system.get_install_path(), self._name)
            super(ConditionalPackage, self).update()            
    # Functions to override
    def _is_system_installed( self ):
        """ Check if package is installed on the system."""
        return False
