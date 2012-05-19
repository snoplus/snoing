#!/usr/bin/env python
# Author P G Jones - 15/05/2012 <p.g.jones@qmul.ac.uk> : First revision
# The GEANT4 packages base class
import LocalPackage
import os
import PackageUtil

class Geant4Pre5( LocalPackage.LocalPackage ):
    """ Base geant4 installer for pre 4.9.5 geant versions."""
    def __init__( self, name, cachePath, installPath, graphical, sourceTar, dataTars, clhepDependency, xercesDependency ):
        """ Initialise the geant4 package."""
        super( Geant4Pre5, self ).__init__( name, cachePath, installPath, graphical )
        self._SourceTar = sourceTar
        self._DataTars = dataTars
        self._ClhepDependency = clhepDependency
        self._XercesDependency = xercesDependency
        return
    # Functions to override
    def CheckState( self ):
        """ Derived classes should override this to ascertain the package status, downloaded? installed?"""
        if os.path.exists( os.path.join( self._CachePath, self._DataTars[-1] ) ):
            self._SetMode( 1 ) # Downloaded 
        sys = os.uname()[0] + "-g++"
        if os.path.exists( os.path.join( self.GetInstallPath(), "lib/" + sys + "/libG4event.a" ) ):
            self._SetMode( 2 ) # Installed as well
        return
    def GetDependencies( self ):
        """ Return the dependency names as a list of names."""
        return [ "make", "g++", "gcc", self._ClhepDependency ]
    def _Download( self ):
        """ Derived classes should override this to download the package."""
        result = PackageUtil.DownloadFile( "http://geant4.web.cern.ch/geant4/support/source/" + self._SourceTar )
        for dataTar in self._DataTars:
            result = result && PackageUtil.DownloadFile( "http://geant4.web.cern.ch/geant4/support/source/" + dataTar )
        return result
    def _Install( self ):
        """ Derived classes should override this to install the package, should install only when finished. Return True on success."""
        PackageUtil.UnTarFile( self._SourceTar, self.GetInstallPath(), 1 )
        for dataTar in self._DataTars:
            PackageUtil.UnTarFile( dataTar, os.path.join( self.GetInstallPath(), "data" ), 0 )
        self.WriteGeant4ConfigFile()
        result = PackageUtil.ExecuteSimpleCommand( './Configure', ['-incflags', '-build', '-d', '-e', '-f', "geant4-snoing-config.sh"], None, self.GetInstallPath() )
        result = result && PackageUtil.ExecuteSimpleCommand( './Configure', ['-incflags', '-install', '-d', '-e', '-f', "geant4-snoing-config.sh"], None, self.GetInstallPath() )
        result = result && PackageUtil.ExecuteSimpleCommand( './Configure', [], None, self.GetInstallPath() )
        return result
    def WriteGeant4ConfigFile( self ):
        """ Write the relevant geant4 configuration file, nasty function."""
        clhepPath = self._DependencyPaths[self._ClhepDependency]
        sys = os.uname()[0]
        configText = "g4clhep_base_dir='%s'\ng4clhep_include_dir='%s'\ng4clhep_lib_dir='%s'\ng4data='%s'\ng4install='%s'\ng4osname='%s'\ng4system='%s'\n" % ( clhepPath, os.path.join( clhepPath, "include" ), os.path.join( clhepPath, "lib" ), os.path.join( self.GetInstallPath(), "data" ), self.GetInstallPath(), sys, sys + "-g++" )
        configText += "g4clhep_lib='CLHEP'\ng4compiler='g++'\ng4debug='n'\nd_portable='define'\ng4global='n'\ng4granular='y'\ng4include=''\ng4includes_flag='y'\ng4lib_build_shared='y'\ng4lib_build_static='y'\ng4lib_use_granular='y'\ng4lib_use_shared='n'\ng4lib_use_static='y'\ng4make='make'\ng4ui_build_gag_session='y'\ng4ui_build_terminal_session='y'\ng4ui_build_win32_session='n'\ng4ui_build_xaw_session='n'\ng4ui_build_xm_session='y'\ng4ui_use_gag='y'\ng4ui_use_tcsh='y'\ng4ui_use_terminal='y'\ng4ui_use_win32='n'\ng4ui_use_xaw='n'\ng4vis_build_oiwin32_driver='n'\ng4vis_build_oix_driver='n'\ng4vis_build_openglwin32_driver='n'\ng4vis_use_oiwin32='n'\ng4vis_use_oix='n'\ng4vis_use_openglwin32='n'\ng4w_use_g3tog4='n'\ng4wanalysis_build=''\ng4wanalysis_build_jas=''\ng4wanalysis_build_lab=''\ng4wanalysis_build_lizard=''\ng4wanalysis_use='n'\ng4wanalysis_use_jas=''\ng4wanalysis_use_lab=''\ng4wanalysis_use_lizard=''\ng4wlib_build_g3tog4='n'\n"
        if self._Graphical:
            xercesPath = self._DependencyPaths[self._XercesDependency]
            configText += "g4vis_build_asciitree_driver='y'\ng4vis_build_dawn_driver='y'\ng4vis_build_dawnfile_driver='y'\ng4vis_build_openglx_driver='y'\ng4vis_build_openglxm_driver='y'\ng4vis_build_raytracer_driver='y'\ng4vis_build_vrml_driver='y'\ng4vis_build_vrmlfile_driver='y'\ng4vis_oglhome='/usr/X11R6/'\ng4vis_use_asciitree='y'\ng4vis_use_dawn='y'\ng4vis_use_dawnfile='y'\ng4vis_use_openglx='y'\ng4vis_use_openglxm='y'\ng4vis_use_raytracer='y'\ng4vis_use_vrml='y'\ng4vis_use_vrmlfile='y'\ng4lib_build_gdml='y'\ng4gdml_xercesc_root='%s'\nwith_xercesc_root='%s'" % ( xercesPath, xercesPath )
        else:
            configText += "g4vis_build_asciitree_driver='n'\ng4vis_build_dawn_driver='n'\ng4vis_build_dawnfile_driver='n'\ng4vis_build_openglx_driver='n'\ng4vis_build_openglxm_driver='n'\ng4vis_build_raytracer_driver='n'\ng4vis_build_vrml_driver='n'\ng4vis_build_vrmlfile_driver='n'\ng4vis_oglhome=''\ng4vis_use_asciitree='n'\ng4vis_use_dawn='n'\ng4vis_use_dawnfile='n'\ng4vis_use_openglx='n'\ng4vis_use_openglxm='n'\ng4vis_use_raytracer='n'\ng4vis_use_vrml='n'\ng4vis_use_vrmlfile='n'\ng4vis_none='1'\n"
        configFile = open( os.path.join( self.GetInstallPath(), "geant4-snoing-config.sh" ), "w" )
        configFile.write( configText )
        configFile.close()
