#!/usr/bin/env python
# Author P G Jones - 22/06/2012 <p.g.jones@qmul.ac.uk> : First revision
# The ROOT prerequisites
import CommandPackage
import LibraryPackage

class Pthread( LibraryPackage.LibraryPackage ):
    """ Package for the pthread library."""
    def __init__( self ):
        super( Pthread, self ).__init__( "pthread", "Install pthread-dev on this system.", "pthread" )
        return

class OpenGL( LibraryPackage.LibraryPackage ):
    """ Package for the pthread library."""
    def __init__( self ):
        super( OpenGL, self ).__init__( "opengl", "Install openGL on this system.", "GL", "GL/gl.h" )
        return

class Xlib( LibraryPackage.LibraryPackage ):
    """ Package for the pthread library. 
    I'm not sure this is a real thing, just a X11 header file?"""
    def __init__( self ):
        super( Xlib, self ).__init__( "xlib", "Install xlib on this system.", "X11", "X11/Xlib.h" )
        return

class XRandR( LibraryPackage.LibraryPackage ):
    """ Package for the pthread library."""
    def __init__( self ):
        super( XRandR, self ).__init__( "xrandr", "Install libXrandr on this system.", "Xrandr", "X11/extensions/Xrandr.h")
        return

class Freetype( LibraryPackage.LibraryPackage ):
    """ Package for the freetype library."""
    def __init__( self ):
        super( Freetype, self ).__init__( "freetype", "Install freetype dev on this system.", "freetype" )#, "freetype.h" )
        return

class Glew( LibraryPackage.LibraryPackage ):
    """ Package for the glew library."""
    def __init__( self ):
        super( Glew, self ).__init__( "glew", "Install glew on this system.", "GLEW", "GL/glew.h" )
        return

class JPEG( LibraryPackage.LibraryPackage ):
    """ Package for the pthread library."""
    def __init__( self ):
        super( JPEG, self ).__init__( "jpeg", "Install jpeg dev on this system.", "jpeg")#, "jpeglib.h" )
        return

class SndFile( LibraryPackage.LibraryPackage ):
    """ Package for the SNDFILE library."""
    def __init__( self ):
        super( SndFile, self ).__init__( "sndfile", "Install sndfile dev on this system.", "sndfile", "sndfile.h" )
        return

class OpenAL( LibraryPackage.LibraryPackage ):
    """ Package for the openAL library."""
    def __init__( self ):
        super( OpenAL, self ).__init__( "openal", "Install openAL dev on this system.", "openal", "AL/al.h" )
        return
