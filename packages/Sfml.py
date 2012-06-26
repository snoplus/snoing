#!/usr/bin/env python
# Author O Wasalski - 07/06/2012 <wasalski@berkeley.edu> : First revision, new file
# Author P G Jones - 23/06/2012 <p.g.jones@qmul.ac.uk> : Refactor of Package Structure 
# The SFML packages base class
import LocalPackage
import os
import PackageUtil

class Sfml( LocalPackage.LocalPackage ):
    """ Base sfml installer package."""
    def __init__( self, name, tarName ):
        """ Initialise sfml with the tarName."""
        super( Sfml, self ).__init__( name, True ) # This is graphical only
        self._TarName = tarName
        return

    def GetDependencies( self ):
        """ Return the required dependencies."""
        return ["cmake", "pthread", "opengl", "xlib", "xrandr", "freetype", "glew", "jpeg", "sndfile", "openal"]
    def _IsDownloaded( self ):
        """ Has the tar file been downloaded."""
        return os.path.exists( os.path.join( PackageUtil.kCachePath, self._TarName ) )
    def _IsInstalled( self ):
        """ Has sfml been installed."""
        libDir = os.path.join( self.GetInstallPath(), "lib" )
        libs = [ "audio", "graphics", "network", "system", "window" ]
        libPaths = [ libDir + "/libsfml-" + lib + ".so" for lib in libs ]
        return PackageUtil.All( [ os.path.isfile( libPath ) for libPath in libPaths ] )
    def _Download( self ):
        """ Download the tar file."""
        self._DownloadPipe += PackageUtil.DownloadFile( "https://github.com/LaurentGomila/SFML/tarball/" + self._TarName )
        return
    def _Install( self ):
        """ Install sfml."""
        env = os.environ
        installPath = self.GetInstallPath()
        PackageUtil.UnTarFile( self._TarName, self.GetInstallPath(), 1 )
        cmakeCommand = "cmake"
        if self._DependencyPaths["cmake"] is not None: # Special cmake installed
            cmakeCommand = "%s/bin/cmake" % self._DependencyPaths["cmake"]
        self._InstallPipe += PackageUtil.ExecuteSimpleCommand( cmakeCommand, [ "-DCMAKE_INSTALL_PREFIX:PATH=$PWD" ], env, self.GetInstallPath() )
        self._InstallPipe += PackageUtil.ExecuteSimpleCommand( "make", [], env, self.GetInstallPath() )
        return
