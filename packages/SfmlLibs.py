#!/usr/bin/env python
# Author P G Jones - 22/06/2012 <p.g.jones@qmul.ac.uk> : First revision
# The ROOT prerequisites
import CommandPackage
import LibraryPackage

class Pthread( LibraryPackage.LibraryPackage ):
    """ Package for the pthread library."""
    def __init__( self ):
        super( Pthread, self ).__init__( "pthread", "pthread" )
        return

class OpenGL( LibraryPackage.LibraryPackage ):
    """ Package for the pthread library."""
    def __init__( self ):
        super( OpenGL, self ).__init__( "opengl", "GL", "GL/gl.h" )
        return

class Xlib( LibraryPackage.LibraryPackage ):
    """ Package for the pthread library."""
    def __init__( self ):
        super( Xlib, self ).__init__( "xlib", "xlib" )
        return

class XRandR( LibraryPackage.LibraryPackage ):
    """ Package for the pthread library."""
    def __init__( self ):
        super( XRandR, self ).__init__( "xrandr", "Xrandr", "X11/extensions/Xrandr.h")
        return

class Freetype( LibraryPackage.LibraryPackage ):
    """ Package for the freetype library."""
    def __init__( self ):
        super( Freetype, self ).__init__( "freetype", "freetype", "freetype.h" )
        return

class Glew( LibraryPackage.LibraryPackage ):
    """ Package for the glew library."""
    def __init__( self ):
        super( Glew, self ).__init__( "glew", "GLEW", "GL/glew.h" )
        return

class JPEG( LibraryPackage.LibraryPackage ):
    """ Package for the pthread library."""
    def __init__( self ):
        super( JPEG, self ).__init__( "jpeg", "jpeg", "jpeglib.h" )
        return

class SndFile( LibraryPackage.LibraryPackage ):
    """ Package for the SNDFILE library."""
    def __init__( self ):
        super( SndFile, self ).__init__( "sndfile", "sndfile", "sndfile.h" )
        return

class OpenAL( LibraryPackage.LibraryPackage ):
    """ Package for the openAL library."""
    def __init__( self ):
        super( OpenAL, self ).__init__( "openal", "openal", "AL/al.h" )
        return
