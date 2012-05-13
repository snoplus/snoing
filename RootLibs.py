#!/usr/bin/env python
# Author P G Jones - 13/05/2012 <p.g.jones@qmul.ac.uk> : First revision
# The ROOT prerequisites
import SystemPackage

class Make( SystemPackage.SystemPackage ):
    """ Package for the make command."""
    def __init__( self ):
        """ Initialise the package, set the name."""
        super( Make, self ).__init__( "make" )
        return
    def CheckState( self ):
        """ Check if make is installed, look for make."""
        if self._FindLibrary( "make" ) == None:
            print "Make is not installed."
        else:
            self._Mode = 1

class Gpp( SystemPackage.SystemPackage ):
    """ Package for the make command."""
    def __init__( self ):
        """ Initialise the package, set the name."""
        super( Gpp, self ).__init__( "g++" )
        return
    def CheckState( self ):
        """ Check if g++ is installed, look for g++."""
        if self._FindLibrary( "g++" ) == None:
            print "g++ is not installed."
        else:
            self._Mode = 1

class GCC( SystemPackage.SystemPackage ):
    """ Package for the make command."""
    def __init__( self ):
        """ Initialise the package, set the name."""
        super( GCC, self ).__init__( "gcc" )
        return
    def CheckState( self ):
        """ Check if gcc is installed, look for gcc."""
        if self._FindLibrary( "gcc" ) == None:
            print "gcc is not installed."
        else:
            self._Mode = 1


