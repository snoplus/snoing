#!/usr/bin/env python
#
# SystemException, PackageException
#
# Exceptions raised by the system module and the pakcagemanager module.
#
# Author P G Jones - 21/06/2012 <p.g.jones@qmul.ac.uk> : First revision
# Author P G Jones - 02/08/2012 <p.g.jones@qmul.ac.uk> : New exception
# Author P G Jones - 23/06/2012 <p.g.jones@qmul.ac.uk> : Major refactor of snoing.
####################################################################################################

class SystemException(Exception):
    """ A custom exception containing the error type and details.."""
    def __init__(self, error, details):
        """ Call the base class constructor and save the details."""
        Exception.__init__(self, error)
        self.Details = details

class PackageException(Exception):
    """ A custom exception containing the message and package name.."""
    def __init__(self, message, package):
        """ Call the base class constructor."""
        Exception.__init__(self, message)
        self.Package = package

