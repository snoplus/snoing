#!/usr/bin/env python
# Author P G Jones - 22/06/2012 <p.g.jones@qmul.ac.uk> : First revision
# The General shared prerequisites
import CommandPackage

class Git( CommandPackage.CommandPackage ):
    """ Package for the git command."""
    def __init__( self ):
        """ Initialise the package, set the name."""
        super( Git, self ).__init__( "git", "Install git on this system." )
        return
