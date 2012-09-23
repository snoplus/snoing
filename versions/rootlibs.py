#!/usr/bin/env python
#
# Make, Gpp, GCC, Ld, X11, Xpm, Xft, Xext
#
# Required root libraries.
#
# Author P G Jones - 13/05/2012 <p.g.jones@qmul.ac.uk> : First revision
# Author P G Jones - 13/06/2012 <p.g.jones@qmul.ac.uk> : Added extra root libraries
# Author P G Jones - 22/09/2012 <p.g.jones@qmul.ac.uk> : Major refactor of snoing.
####################################################################################################
import commandpackage
import librarypackage

class Make(commandpackage.CommandPackage):
    """ Package for the make command."""
    def __init__(self, system):
        """ Initialise the package, set the name."""
        super(Make, self).__init__("make", system, "Install the 'make' package on this system")

class Gpp(commandpackage.CommandPackage):
    """ Package for the g++ command."""
    def __init__(self, system):
        """ Initialise the package, set the name."""
        super(Gpp, self).__init__("g++", system, 
                                  "Install a g++ compiler on this system (build-essential on linux)")

class GCC(commandpackage.CommandPackage):
    """ Package for the gcc command."""
    def __init__(self, system):
        """ Initialise the package, set the name."""
        super(GCC, self).__init__("gcc", system, 
                                  "Install a gcc compiler on this system (build-essential on linux)")

class Ld(commandpackage.CommandPackage):
    """ Package for the ld command."""
    def __init__(self, system):
        """ Initialise the package, set the name."""
        super(Ld, self).__init__("ld", system, "Install the ld tool on this system.")

class X11(librarypackage.LibraryPackage):
    """ Package for the x11-dev library."""
    def __init__(self, system):
        super(X11, self).__init__("X11", system, "Install X11-dev on this system.", 
                                  "X11", ["X11/Xlib.h"])

class Xpm(librarypackage.LibraryPackage):
    """ Package for the xpm-dev library."""
    def __init__(self, system):
        super(Xpm, self).__init__("Xpm", system, "Install Xpm-dev on this system.", 
                                  "Xpm", ["X11/xpm.h"])

class Xft(librarypackage.LibraryPackage):
    """ Package for the xft-dev library."""
    def __init__(self, system):
        super(Xft, self).__init__("Xft", system, "Install Xft-dev on this system.", "Xft")
        #"X11/Xft/Xft.h")

class Xext(librarypackage.LibraryPackage):
    """ Package for the xext-dev library."""
    def __init__(self, system):
        super(Xext, self).__init__("Xext", system, "Install the X11 extensions dev on this system.", 
                                   "Xext", ["X11/extensions/shape.h"])
