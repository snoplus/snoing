#!/usr/bin/env python
#
# Cmake
#
# The cmake package installer
#
# Author P G Jones - 22/06/2012 <p.g.jones@qmul.ac.uk> : First revision
# Author P G Jones - 24/09/2012 <p.g.jones@qmul.ac.uk> : Major refactor of snoing.
####################################################################################################

import conditionalpackage
import os

class Cmake(conditionalpackage.ConditionalPackage):
    """Cmake install package."""

    def __init__(self, name, system, tar_name):
        """Initlaise the Cmake package."""
        super(Cmake, self).__init__(name, system)
        self._tar_name = tar_name

    def get_dependencies(self):
        """Return the dependencies."""
        return []

    def _is_system_installed(self):
        """Check if installed on the system, will require at least version 2.8.1."""

        if self._system.find_library('cmake') is not None:  # A version of cmake exists
            version_string = self._system.execute_command('cmake', ['--version']).split()[2]
            version_numbers = version_string.split('.')

            # Check cmake 2.8.1 or above is installed
            if int(version_numbers[0]) < 2:  # No good
                return False
            elif (len(version_numbers) == 2
                    and int(version_numbers[0]) == 2
                    and int(version_numbers[1][0]) < 8):  # <2.8 bad
                return False
            elif (len(version_numbers) == 3
                    and int(version_numbers[0]) == 2
                    and int(version_numbers[1]) == 8
                    and int(version_numbers[2][0]) < 1):
                return False
            else:  # All others are good
                return True

    def _is_downloaded(self):
        """Check if tar file exists."""
        return self._system.file_exists(self._tar_name)

    def _is_installed(self):
        """Check if installed."""
        return self._system.file_exists('cmake', os.path.join(self.get_install_path(), 'bin'))

    def _install(self):
        """Install the 2.8 version."""
        self._system.untar_file(self._tar_name, self.get_install_path(), 1)
        self._system.execute_command('./bootstrap', ['--prefix=%s' % self.get_install_path()],
                                     cwd=self.get_install_path())
        self._system.execute_command('make', cwd=self.get_install_path())
        self._system.execute_command('make', ['install'], cwd=self.get_install_path())
