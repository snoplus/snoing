#!/usr/bin/env python
# Author P G Jones - 15/05/2012 <p.g.jones@qmul.ac.uk> : First revision
# Author P G Jones - 21/05/2012 <p.g.jones@qmul.ac.uk> : Add Post 4.9.5 version
# The GEANT4 packages base class
import LocalPackage
import os
import PackageUtil

class Geant4Post5( LocalPackage.LocalPackage ):
    """ Base geant4 installer for post 4.9.5 geant versions. This is sooooo much nicer"""
    def __init__( self, name, sourceTar, clhepDependency, xercesDependency ):
        """ Initialise the geant4 package."""
        super( Geant4Post5, self ).__init__( name, False ) # Not graphical only
        self._SourceTar = sourceTar
        self._XercesDependency = xercesDependency
        self._ClhepDependency = clhepDependency
        return

    def GetDependencies( self ):
        """ Return the dependency names as a list of names."""
        dependencies = [ "make", "g++", "gcc", "cmake", self._XercesDependency, self._ClhepDependency ]
        if PackageUtil.kGraphical:
            dependencies.extend( ["Xm", "Xt", "opengl", "Xmu", "Xi"] )
        return dependencies
    def _IsDownloaded( self ):
        """ Check if the tar file has been downloaded."""
        return os.path.exists( os.path.join( PackageUtil.kCachePath, self._SourceTar ) )
    def _IsInstalled( self ):
        """ Check if the package has been installed."""
        installed = PackageUtil.LibraryExists( os.path.join( self.GetInstallPath(), "lib"), "libG4event" ) or \
            PackageUtil.LibraryExists( os.path.join( self.GetInstallPath(), "lib64" ), "libG4event" )
        if PackageUtil.kGraphical:
            installed = installed and ( PackageUtil.LibraryExists( os.path.join( self.GetInstallPath(), "lib" ), "libG4UIbasic" ) or \
                PackageUtil.LibraryExists( os.path.join( self.GetInstallPath(), "lib64" ), "libG4UIbasic" ) )
        return installed
    def _Download( self ):
        """ Derived classes should override this to download the package."""
        self._DownloadPipe = PackageUtil.DownloadFile( "http://geant4.web.cern.ch/geant4/support/source/" + self._SourceTar )
        return
    def _Install( self ):
        """ Install geant4, using cmake."""
        sourcePath = os.path.join( PackageUtil.kInstallPath, "%s-source" % self._Name )
        PackageUtil.UnTarFile( self._SourceTar, sourcePath, 1 )
        if not os.path.exists( self.GetInstallPath() ):
            os.makedirs( self.GetInstallPath() )
        cmakeOpts = [ "-DCMAKE_INSTALL_PREFIX=%s" % self.GetInstallPath(), \
                          "-DCLHEP_ROOT_DIR=%s" % self._DependencyPaths[self._ClhepDependency], \
                          "-DXERCESC_ROOT_DIR=%s" % self._DependencyPaths[self._XercesDependency], \
                          "-DGEANT4_INSTALL_DATA=ON", \
                          "-DCLHEP_CONFIG_EXECUTABLE=%s" % os.path.join( self._DependencyPaths[self._ClhepDependency], "clhep-config" ) ]
        if PackageUtil.kGraphical:
            cmakeOpts.extend( [ "-DGEANT4_USE_XM=ON", "-DGEANT4_USE_OPENGL_X11=ON", "-DGEANT4_USE_RAYTRACER_X11=ON" ]  )
        cmakeOpts.extend( [ sourcePath ] )
        cmakeCommand = "cmake"
        if self._DependencyPaths["cmake"] is not None: # Special cmake installed
            cmakeCommand = "%s/bin/cmake" % self._DependencyPaths["cmake"]
        self._InstallPipe += PackageUtil.ExecuteSimpleCommand( cmakeCommand, cmakeOpts, None, self.GetInstallPath() )
        self._InstallPipe += PackageUtil.ExecuteSimpleCommand( "make", [], None, self.GetInstallPath() )
        self._InstallPipe += PackageUtil.ExecuteSimpleCommand( "make", ['install'], None, self.GetInstallPath() )
        return

class Geant4Pre5( LocalPackage.LocalPackage ):
    """ Base geant4 installer for pre 4.9.5 geant versions."""
    def __init__( self, name, sourceTar, dataTars, clhepDependency, xercesDependency ):
        """ Initialise the geant4 package."""
        super( Geant4Pre5, self ).__init__( name, False ) # Not graphical only
        self._ClhepDependency = clhepDependency
        self._DataTars = dataTars
        self._SourceTar = sourceTar
        self._XercesDependency = xercesDependency
        return

    def GetDependencies( self ):
        """ Return the dependency names as a list of names."""
        dependencies = [ "make", "g++", "gcc", self._XercesDependency, self._ClhepDependency ]
        if PackageUtil.kGraphical:
            dependencies.extend( ["Xm", "Xt", "opengl", "Xmu", "Xi"] )
        return dependencies
    def _IsDownloaded( self ):
        """ Check tar files have been downloaded."""
        downloaded = PackageUtil.All( [ os.path.isfile( os.path.join( PackageUtil.kCachePath, tar ) ) for tar in self._DataTars ] )
        downloaded = downloaded and os.path.exists( os.path.join( PackageUtil.kCachePath, self._SourceTar ) )
        return downloaded
    def _IsInstalled( self ):
        """ Check geant has been installed."""
        sys = os.uname()[0] + "-g++"
        installed = PackageUtil.LibraryExists( os.path.join( self.GetInstallPath(), "lib/" + sys ), "libG4event" ) and \
            PackageUtil.LibraryExists( os.path.join( self.GetInstallPath(), "lib/" + sys ),  "libG4UIbasic" )
        return installed
    def _Download( self ):
        """ Derived classes should override this to download the package."""
        self._DownloadPipe = PackageUtil.DownloadFile( "http://geant4.web.cern.ch/geant4/support/source/" + self._SourceTar )
        for dataTar in self._DataTars:
            self._DownloadPipe += PackageUtil.DownloadFile( "http://geant4.web.cern.ch/geant4/support/source/" + dataTar )
        return
    def _Install( self ):
        """ Derived classes should override this to install the package, should install only when finished. Return True on success."""
        self._InstallPipe += PackageUtil.UnTarFile( self._SourceTar, self.GetInstallPath(), 1 )
        for dataTar in self._DataTars:
            self._InstallPipe += PackageUtil.UnTarFile( dataTar, os.path.join( self.GetInstallPath(), "data" ), 0 )
        self.WriteGeant4ConfigFile()
        self._InstallPipe += PackageUtil.ExecuteSimpleCommand( './Configure', ['-incflags', '-build', '-d', '-e', '-f', "geant4-snoing-config.sh"], None, self.GetInstallPath() )
        self._InstallPipe += PackageUtil.ExecuteSimpleCommand( './Configure', ['-incflags', '-install', '-d', '-e', '-f', "geant4-snoing-config.sh"], None, self.GetInstallPath() )
        try:
            self._InstallPipe += PackageUtil.ExecuteSimpleCommand( './Configure', [], None, self.GetInstallPath() )
        except Exception: # Geant4 configure always fails, it is annoying
            pass
        return 
    def WriteGeant4ConfigFile( self ):
        """ Write the relevant geant4 configuration file, nasty function."""
        clhepPath = self._DependencyPaths[self._ClhepDependency]
        sys = os.uname()[0]
        configText = "g4clhep_base_dir='%s'\ng4clhep_include_dir='%s'\ng4clhep_lib_dir='%s'\ng4data='%s'\ng4install='%s'\ng4osname='%s'\ng4system='%s'\n" % ( clhepPath, os.path.join( clhepPath, "include" ), os.path.join( clhepPath, "lib" ), os.path.join( self.GetInstallPath(), "data" ), self.GetInstallPath(), sys, sys + "-g++" )
        configText += "g4clhep_lib='CLHEP'\ng4compiler='g++'\ng4debug='n'\nd_portable='define'\ng4global='n'\ng4granular='y'\ng4include=''\ng4includes_flag='y'\ng4lib_build_shared='y'\ng4lib_build_static='y'\ng4lib_use_granular='y'\ng4lib_use_shared='n'\ng4lib_use_static='y'\ng4make='make'\ng4ui_build_gag_session='y'\ng4ui_build_terminal_session='y'\ng4ui_build_win32_session='n'\ng4ui_build_xaw_session='n'\ng4ui_use_gag='y'\ng4ui_use_tcsh='y'\ng4ui_use_terminal='y'\ng4ui_use_win32='n'\ng4ui_use_xaw='n'\ng4vis_build_oiwin32_driver='n'\ng4vis_build_oix_driver='n'\ng4vis_build_openglwin32_driver='n'\ng4vis_use_oiwin32='n'\ng4vis_use_oix='n'\ng4vis_use_openglwin32='n'\ng4w_use_g3tog4='n'\ng4wanalysis_build=''\ng4wanalysis_build_jas=''\ng4wanalysis_build_lab=''\ng4wanalysis_build_lizard=''\ng4wanalysis_use='n'\ng4wanalysis_use_jas=''\ng4wanalysis_use_lab=''\ng4wanalysis_use_lizard=''\ng4wlib_build_g3tog4='n'\n"
        xercesPath = self._DependencyPaths[self._XercesDependency]
        if PackageUtil.kGraphical:
            configText += "g4ui_build_xm_session='y'\ng4ui_use_xm='y'\ng4vis_build_asciitree_driver='y'\ng4vis_build_dawn_driver='y'\ng4vis_build_dawnfile_driver='y'\ng4vis_build_openglx_driver='y'\ng4vis_build_openglxm_driver='y'\ng4vis_build_raytracer_driver='y'\ng4vis_build_vrml_driver='y'\ng4vis_build_vrmlfile_driver='y'\ng4vis_oglhome='/usr'\noglhome='/usr'\ng4vis_use_asciitree='y'\ng4vis_use_dawn='y'\ng4vis_use_dawnfile='y'\ng4vis_use_openglx='y'\ng4vis_use_openglxm='y'\ng4vis_use_raytracer='y'\ng4vis_use_vrml='y'\ng4vis_use_vrmlfile='y'\ng4lib_build_gdml='y'\ng4gdml_xercesc_root='%s'\nwith_xercesc_root='%s'" % ( xercesPath, xercesPath )
        else:
            configText += "g4ui_build_xm_session='n'\ng4ui_use_xm='n'\ng4vis_build_asciitree_driver='n'\ng4vis_build_dawn_driver='n'\ng4vis_build_dawnfile_driver='n'\ng4vis_build_openglx_driver='n'\ng4vis_build_openglxm_driver='n'\ng4vis_build_raytracer_driver='n'\ng4vis_build_vrml_driver='n'\ng4vis_build_vrmlfile_driver='n'\ng4vis_oglhome=''\ng4vis_use_asciitree='n'\ng4vis_use_dawn='n'\ng4vis_use_dawnfile='n'\ng4vis_use_openglx='n'\ng4vis_use_openglxm='n'\ng4vis_use_raytracer='n'\ng4vis_use_vrml='n'\ng4vis_use_vrmlfile='n'\ng4vis_none='1'\ng4lib_build_gdml='y'\ng4gdml_xercesc_root='%s'\nwith_xercesc_root='%s'" % ( xercesPath, xercesPath )
        configFile = open( os.path.join( self.GetInstallPath(), "geant4-snoing-config.sh" ), "w" )
        configFile.write( configText )
        configFile.close()
