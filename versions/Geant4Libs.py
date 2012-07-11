#!/usr/bin/env python
# Author P G Jones - 22/06/2012 <p.g.jones@qmul.ac.uk> : First revision
# The Geant4 prerequisites
import CommandPackage
import LibraryPackage
import PackageUtil

class Xt( LibraryPackage.LibraryPackage ):
    """ Package for the Xt library."""
    def __init__( self ):
        if PackageUtil.kMac:
            super( Xt, self ).__init__( "Xt", "Install Xt-dev on this system.", "Xt", "X11/include/X11/Intrinsic.h" )
        else:
            super( Xt, self ).__init__( "Xt", "Install Xt-dev on this system.", "Xt", "X11/Intrinsic.h" )
        return

class Xmu( LibraryPackage.LibraryPackage ):
    """ Package for the Xmu library."""
    def __init__( self ):
        if PackageUtil.kMac:
            super( Xmu, self ).__init__( "Xmu", "Install Xmu-dev on this system.", "Xmu", "X11/include/X11/Xmu/Xmu.h" )
        else:
            super( Xmu, self ).__init__( "Xmu", "Install Xmu-dev on this system.", "Xmu", "X11/Xmu/Xmu.h" )
        return

class Xi( LibraryPackage.LibraryPackage ):
    """ Package for the Xi library. """
    def __init__( self ):
        super( Xi, self ).__init__( "Xi", "Install Xi-dev on this system.", "Xi", "X11/extensions/XI.h" )
