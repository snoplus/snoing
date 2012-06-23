#!/usr/bin/env python
# Author P G Jones - 22/06/2012 <p.g.jones@qmul.ac.uk> : First revision
# The General shared prerequisites
import CommandPackage
import LibraryPackage

class Git( CommandPackage.CommandPackage ):
    """ Package for the git command."""
    def __init__( self ):
        """ Initialise the package, set the name."""
        super( Git, self ).__init__( "git" )
        return

class Python( LibraryPackage.LibraryPackage ):
    """ Package for the python development library."""
    def __init__( self ):
        super( Python, self ).__init__( "python", "python", "Python.h" )
        return
