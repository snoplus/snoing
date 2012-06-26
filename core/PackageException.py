#!/usr/bin/env python
# Author P G Jones - 21/06/2012 <p.g.jones@qmul.ac.uk> : First revision
# Allows a custom exception to be thrown containing the relevant output

class PackageException( Exception ):
    """ A custom exception containing the message and pipe."""
    def __init__( self, message, pipe ):
        """ Call the base class constructor and save the pipe info."""
        Exception.__init__( self, message )
        self.Pipe = pipe
        return
