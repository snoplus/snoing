#!/usr/bin/env python
# Author P G Jones - 22/06/2012 <p.g.jones@qmul.ac.uk> : First revision
# The General shared prerequisites
import CommandPackage
import LibraryPackage

class Git( CommandPackage.CommandPackage ):
    """ Package for the git command."""
    def __init__( self ):
        """ Initialise the package, set the name."""
        super( Git, self ).__init__( "git", "Install git on this system." )
        return

class PythonDev( LibraryPackage.LibraryPackage ):
    """ Package for the python development library."""
    def __init__( self ):
        super( PythonDev, self ).__init__( "python-dev", "Install python dev on this system.", "python", "Python.h" )
        return

class Python( CommandPackage.CommandPackage ):
    """ Package for the python development library."""
    def __init__( self ):
        super( Python, self ).__init__( "python", "Install python on this system, how on earth is this possible? snoing is written in python")
        return
