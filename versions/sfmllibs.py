#!/usr/bin/env python
#
# Pthread, OpenGL, Xlib, XRandR, Freetype, Glew, JPEG, SndFile, OpenAL
#
# The required packages for sfml.
#
# Author P G Jones - 22/06/2012 <p.g.jones@qmul.ac.uk> : First revision
# Author P G Jones - 22/09/2012 <p.g.jones@qmul.ac.uk> : Major refactor of snoing.
####################################################################################################
import librarypackage

class Pthread(librarypackage.LibraryPackage):
    """ Package for the pthread library."""
    def __init__(self, system):
        super(Pthread, self).__init__("pthread", system, "Install pthread-dev on this system.", 
                                      "pthread")

class OpenGL(librarypackage.LibraryPackage):
    """ Package for the pthread library."""
    def __init__(self, system):
        super(OpenGL, self).__init__("opengl", system, "Install openGL on this system.", "GL", 
                                     "GL/gl.h")

class Xlib(librarypackage.LibraryPackage):
    """ Package for the pthread library. 
    I'm not sure this is a real thing, just a X11 header file?"""
    def __init__(self, system):
        super(Xlib, self).__init__("xlib", system, "Install xlib on this system.", "X11", 
                                   "X11/Xlib.h")

class XRandR(librarypackage.LibraryPackage):
    """ Package for the pthread library."""
    def __init__(self, system):
        super(XRandR, self).__init__("xrandr", system, "Install libXrandr on this system.", 
                                     "Xrandr", "X11/extensions/Xrandr.h")

class Freetype(librarypackage.LibraryPackage):
    """ Package for the freetype library."""
    def __init__(self, system):
        super(Freetype, self).__init__("freetype", system, "Install freetype dev on this system.", 
                                       "freetype")#, "freetype.h")

class Glew(librarypackage.LibraryPackage):
    """ Package for the glew library."""
    def __init__(self, system):
        super(Glew, self).__init__("glew", system, "Install glew on this system.", "GLEW", 
                                   "GL/glew.h")

class JPEG(librarypackage.LibraryPackage):
    """ Package for the pthread library."""
    def __init__(self, system):
        super(JPEG, self).__init__("jpeg", system, "Install jpeg dev on this system.", 
                                   "jpeg")#, "jpeglib.h")

class SndFile(librarypackage.LibraryPackage):
    """ Package for the SNDFILE library."""
    def __init__(self, system):
        super(SndFile, self).__init__("sndfile", system, "Install sndfile dev on this system.", 
                                      "sndfile", "sndfile.h")

class OpenAL(librarypackage.LibraryPackage):
    """ Package for the openAL library."""
    def __init__(self, system):
        if self._system.get_os_type() == system.System.Mac:
            if os.path.exists("/sw/include/OpenAL/alure.h"):
                super(OpenAL, self).__init__("openal", system, 
                                             "Install openAL dev on this system.", "alure", 
                                             "OpenAL/alure.h")
            else:
                super(OpenAL, self).__init__("openal", system, 
                                             "Instal openAL on this system.", "OpenAL", 
                                             "OpenAL.framework/Headers/al.h")
        else:
            super(OpenAL, self).__init__("openal", system, 
                                         "Install openAL dev on this system.", "openal", "AL/al.h")
