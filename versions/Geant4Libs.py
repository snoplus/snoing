#!/usr/bin/env python
# Author P G Jones - 22/06/2012 <p.g.jones@qmul.ac.uk> : First revision
# The Geant4 prerequisites
import CommandPackage
import LibraryPackage

class Xm( LibraryPackage.LibraryPackage ):
    """ Package for the Open Motif/Xm library."""
    def __init__( self ):
        super( Xm, self ).__init__( "Xm", "Xm", "Xm/Xm.h" )
        return

class Xt( LibraryPackage.LibraryPackage ):
    """ Package for the Xt library."""
    def __init__( self ):
        super( Xt, self ).__init__( "Xt", "Xt", "X11/Intrinsic.h" )
        return

class Xmu( LibraryPackage.LibraryPackage ):
    """ Package for the Xmu library."""
    def __init__( self ):
        super( Xmu, self ).__init__( "Xmu", "Xmu", "X11/Xmu/Xmu.h" )
        return
