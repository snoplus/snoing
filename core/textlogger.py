#!/usr/bin/env python
#
# TextLogger
#
# Text logger class, print logging information to the screen
#
# Author P G Jones - 24/08/2012 <p.g.jones@qmul.ac.uk> : First revision
# Author P G Jones - 23/06/2012 <p.g.jones@qmul.ac.uk> : Major refactor of snoing.
####################################################################################################
import logger

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
COMMAND = '\033[96m'
FAIL = '\033[91m'
END = '\033[0m'

class TextLogger(logger.Logger):
    """ Update with pacakages state change information, and convey information to the
    screen in different colours :).
    """
    def __init__(self, local, verbose=False):
        """ Call the base class init."""
        super(TextLogger, self).__init__(local, verbose)
    def package_registered(self, package_name):
        """ Notify that a package has been registered."""
        print HEADER + ("Package %s registered." % package_name) + END
        super(TextLogger, self).package_registered(package_name)
    def package_downloaded(self, package_name):
        """ Notify that a package has been downloaded."""
        print OKBLUE + ("Package %s downloaded." % package_name) + END
        super(TextLogger, self).package_downloaded(package_name)
    def package_installed(self, package_name):
        """ Notify that a package has been installed."""
        print OKGREEN + ("Package %s installed." % package_name) + END
        super(TextLogger, self).package_installed(package_name)
    def package_removed(self, package_name):
        """ Notify that a package has been removed."""
        print WARNING + ("Package %s removed." % package_name) + END
        super(TextLogger, self).package_removed(package_name)
    def package_updated(self, package_name):
        """ Notify that a package has been updated."""
        print OKGREEN + ("Package %s updated." % package_name) + END
        super(TextLogger, self).package_updated(package_name)
    def set_state(self, state, package_name=""):
        """ Notify the current state."""
        print HEADER + state + " " + package_name + END
        super(TextLogger, self).set_state(state, package_name)
    def info(self, info_message):
        """ Output some information."""
        print info_message
        super(TextLogger, self).info(info_message)
    def error(self, error_message):
        """ Notify that an error has occurred."""
        print FAIL + error_message + END
        super(TextLogger, self).error(error_message)
    def command(self, command_message):
        """ Notify which command is being executed."""
        if self._verbose:
            print "\t" + COMMAND + command_message + END
        super(TextLogger, self).command(command_message)
    def detail(self, detail_message):
        """ Notify some detail."""
        if self._verbose:
            print detail_message
        super(TextLogger, self).detail(detail_message)
