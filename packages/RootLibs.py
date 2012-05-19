#!/usr/bin/env python
# Author P G Jones - 13/05/2012 <p.g.jones@qmul.ac.uk> : First revision
# The ROOT prerequisites
import CommandPackage

class Make( CommandPackage.CommandPackage ):
    """ Package for the make command."""
    def __init__( self ):
        """ Initialise the package, set the name."""
        super( Make, self ).__init__( "make" )
        return

class Gpp( CommandPackage.CommandPackage ):
    """ Package for the g++ command."""
    def __init__( self ):
        """ Initialise the package, set the name."""
        super( Gpp, self ).__init__( "g++" )
        return

class GCC( CommandPackage.CommandPackage ):
    """ Package for the gcc command."""
    def __init__( self ):
        """ Initialise the package, set the name."""
        super( GCC, self ).__init__( "gcc" )
        return


