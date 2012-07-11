#!/usr/bin/env python
# Author P G Jones - 13/05/2012 <p.g.jones@qmul.ac.uk> : First revision
# Author P G Jones - 13/06/2012 <p.g.jones@qmul.ac.uk> : Added extra root libraries
# The ROOT prerequisites
import CommandPackage
import LibraryPackage

class Make( CommandPackage.CommandPackage ):
    """ Package for the make command."""
    def __init__( self ):
        """ Initialise the package, set the name."""
        super( Make, self ).__init__( "make", "Install the 'make' package on this system" )
        return

class Gpp( CommandPackage.CommandPackage ):
    """ Package for the g++ command."""
    def __init__( self ):
        """ Initialise the package, set the name."""
        super( Gpp, self ).__init__( "g++", "Install a g++ compiler on this system (build-essential on linux)" )
        return

class GCC( CommandPackage.CommandPackage ):
    """ Package for the gcc command."""
    def __init__( self ):
        """ Initialise the package, set the name."""
        super( GCC, self ).__init__( "gcc", "Install a gcc compiler on this system (build-essential on linux)" )
        return

class Ld( CommandPackage.CommandPackage ):
    """ Package for the ld command."""
    def __init__( self ):
        """ Initialise the package, set the name."""
        super( Ld, self ).__init__( "ld", "Install the ld tool on this system." )
        return

class X11( LibraryPackage.LibraryPackage ):
    """ Package for the x11-dev library."""
    def __init__( self ):
        if PackageUtil.kMac:
            super( X11, self ).__init__( "X11", "Install X11-dev on this system.", "X11", "X11/include/X11/Xlib.h" )
        else:
            super( X11, self ).__init__( "X11", "Install X11-dev on this system.", "X11", "X11/Xlib.h" )
        return

class Xpm( LibraryPackage.LibraryPackage ):
    """ Package for the xpm-dev library."""
    def __init__( self ):
        if PackageUtil.kMac:
            super( Xpm, self ).__init__( "Xpm", "Install Xpm-dev on this system.", "Xpm", "X11/include/X11/xpm.h" )
        else:
            super( Xpm, self ).__init__( "Xpm", "Install Xpm-dev on this system.", "Xpm", "X11/xpm.h" )
        return

class Xft( LibraryPackage.LibraryPackage ):
    """ Package for the xft-dev library."""
    def __init__( self ):
        if PackageUtil.kMac:
            super( Xft, self ).__init__( "Xft", "Install Xft-dev on this system.", "Xft", "X11/include/X11/Xft/Xft.h")
        else:
            super( Xft, self ).__init__( "Xft", "Install Xft-dev on this system.", "Xft")#, "X11/Xft/Xft.h" )
        return

class Xext( LibraryPackage.LibraryPackage ):
    """ Package for the xext-dev library."""
    def __init__( self ):
        super( Xext, self ).__init__( "Xext", "Install the X11 extensions dev on this system.", "Xext", "X11/extensions/shape.h" )
        return
