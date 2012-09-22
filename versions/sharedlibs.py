#!/usr/bin/env python
#
# Git
#
# Checks shared packages exist
#
# Author P G Jones - 22/06/2012 <p.g.jones@qmul.ac.uk> : First revision
# Author P G Jones - 22/09/2012 <p.g.jones@qmul.ac.uk> : Major refactor of snoing.
####################################################################################################
import commandpackage

class Git(commandpackage.CommandPackage):
    """ Package for the git command."""
    def __init__(self, system):
        """ Initialise the package, set the name."""
        super(Git, self).__init__("git", system, "Install git on this system.")
