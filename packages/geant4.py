#!/usr/bin/env python
#
# Geant4Post5, Geant4Pre5
#
# Geant4 installers, big difference after geant4.9.5
#
# Author P G Jones - 15/05/2012 <p.g.jones@qmul.ac.uk> : First revision
# Author P G Jones - 21/05/2012 <p.g.jones@qmul.ac.uk> : Add Post 4.9.5 version
# Author P G Jones - 22/09/2012 <p.g.jones@qmul.ac.uk> : Major refactor of snoing.
####################################################################################################
import localpackage
import installmode
import os
import shutil

class Geant4Post5(localpackage.LocalPackage):
    """ Base geant4 installer for post 4.9.5 geant versions."""
    def __init__(self, name, system, tar_name, xerces_dep):
        """ Initialise the geant4 package."""
        super(Geant4Post5, self).__init__(name, system)
        self._tar_name = tar_name
        self._xerces_dep = xerces_dep
    def get_dependencies(self):
        """ Return the dependency names as a list of names."""
        dependencies = ["make", "g++", "gcc", "cmake", self._xerces_dep]
        if self._system.get_install_mode() == installmode.Graphical:
            dependencies.extend(["Xm", "Xt", "opengl", "Xmu", "Xi"])
        return dependencies
    def _is_downloaded(self):
        """ Check if the tar file has been downloaded."""
        return self._system.file_exists(self._tar_name)
    def _is_installed(self):
        """ Check if the package has been installed."""
        installed = self._system.library_exists("libG4event", os.path.join(self.get_install_path(), "lib")) or \
            self._system.library_exists("libG4event", os.path.join(self.get_install_path(), "lib64"))
        if self._system.get_install_mode() == installmode.Graphical:
            installed = installed and \
                self._system.library_exists("libG4OpenGL", os.path.join(self.get_install_path(), "lib")) or \
                self._system.library_exists("libG4OpenGL", os.path.join(self.get_install_path(), "lib64"))
        return installed
    def _download(self):
        """ Derived classes should override this to download the package."""
        self._system.download_file(
            "http://geant4.web.cern.ch/geant4/support/source/" + self._tar_name)
    def _install(self):
        """ Install geant4, using cmake."""
        source_path = os.path.join(self._system.get_install_path(), "%s-source" % self._name)
        self._system.untar_file(self._tar_name, source_path, 1)
        self._patch_timeout()
        if not os.path.exists(self.get_install_path()):
            os.makedirs(self.get_install_path())
        cmake_opts = ["-DCMAKE_INSTALL_PREFIX=%s" % self.get_install_path(), 
                      "-DGEANT4_INSTALL_DATA=ON"]
        # Now set the environment, if needed
        env = {}
        if self._system.get_install_mode() == installmode.Graphical:
            cmake_opts.extend(["-DGEANT4_USE_XM=ON", "-DGEANT4_USE_OPENGL_X11=ON", 
                               "-DXERCESC_ROOT_DIR=%s" % self._dependency_paths[self._xerces_dep], 
                               "-DGEANT4_USE_RAYTRACER_X11=ON" ])
            env = {'G4VIS_BUILD_VRML_DRIVER' : "1", 'G4VIS_BUILD_OPENGLX_DRIVER' : "1", 
                   'G4VIS_BUILD_OPENGLXM_DRIVER' : "1", 'G4VIS_BUILD_DAWN_DRIVER' : "1" }
        cmake_opts.extend([source_path])
        cmake_command = "cmake"
        if self._dependency_paths["cmake"] is not None: # Special cmake installed
            cmake_command = "%s/bin/cmake" % self._dependency_paths["cmake"]
        self._system.configure_command(cmake_command, cmake_opts, self.get_install_path(), env, config_type="geant4")
        self._system.execute_command("make", [], self.get_install_path(), env)
        self._system.execute_command("make", ['install'], self.get_install_path(), env)
        

class Geant495(localpackage.LocalPackage):
    """ Base geant4 installer for post 4.9.4 geant versions. This is sooooo much nicer"""
    def __init__(self, name, system, tar_name, clhep_dep, xerces_dep):
        """ Initialise the geant4 package."""
        super(Geant495, self).__init__(name, system)
        self._tar_name = tar_name
        self._xerces_dep = xerces_dep
        self._clhep_dep = clhep_dep
    def get_dependencies(self):
        """ Return the dependency names as a list of names."""
        dependencies = ["make", "g++", "gcc", "cmake", self._xerces_dep, self._clhep_dep]
        if self._system.get_install_mode() == installmode.Graphical:
            dependencies.extend(["Xm", "Xt", "opengl", "Xmu", "Xi"])
        return dependencies
    def _is_downloaded(self):
        """ Check if the tar file has been downloaded."""
        return self._system.file_exists(self._tar_name)
    def _is_installed(self):
        """ Check if the package has been installed."""
        installed = self._system.library_exists("libG4event", os.path.join(self.get_install_path(), "lib")) or \
            self._system.library_exists("libG4event", os.path.join(self.get_install_path(), "lib64"))
        if self._system.get_install_mode() == installmode.Graphical:
            installed = installed and \
                self._system.library_exists("libG4OpenGL", os.path.join(self.get_install_path(), "lib")) or \
                self._system.library_exists("libG4OpenGL", os.path.join(self.get_install_path(), "lib64"))
        return installed
    def _download(self):
        """ Derived classes should override this to download the package."""
        self._system.download_file(
            "http://geant4.web.cern.ch/geant4/support/source/" + self._tar_name)
    def _install(self):
        """ Install geant4, using cmake."""
        source_path = os.path.join(self._system.get_install_path(), "%s-source" % self._name)
        self._system.untar_file(self._tar_name, source_path, 1)
        self._patch_timeout()
        if not os.path.exists(self.get_install_path()):
            os.makedirs(self.get_install_path())
        cmake_opts = ["-DCMAKE_INSTALL_PREFIX=%s" % self.get_install_path(), 
                      "-DCLHEP_ROOT_DIR=%s" % self._dependency_paths[self._clhep_dep], 
                      "-DXERCESC_ROOT_DIR=%s" % self._dependency_paths[self._xerces_dep], 
                      "-DGEANT4_INSTALL_DATA=ON", 
                      "-DCLHEP_CONFIG_EXECUTABLE=%s" % \
                          os.path.join(self._dependency_paths[self._clhep_dep], "bin/clhep-config")]
        # Now set the environment, if needed
        env = {}
        if self._system.get_install_mode() == installmode.Graphical:
            cmake_opts.extend(["-DGEANT4_USE_XM=ON", "-DGEANT4_USE_OPENGL_X11=ON", 
                               "-DGEANT4_USE_RAYTRACER_X11=ON" ])
            env = {'G4VIS_BUILD_VRML_DRIVER' : "1", 'G4VIS_BUILD_OPENGLX_DRIVER' : "1", 
                   'G4VIS_BUILD_OPENGLXM_DRIVER' : "1", 'G4VIS_BUILD_DAWN_DRIVER' : "1" }
        cmake_opts.extend([source_path])
        cmake_command = "cmake"
        if self._dependency_paths["cmake"] is not None: # Special cmake installed
            cmake_command = "%s/bin/cmake" % self._dependency_paths["cmake"]
        self._system.configure_command(cmake_command, cmake_opts, self.get_install_path(), env, config_type="geant4")
        self._system.execute_command("make", [], self.get_install_path(), env)
        self._system.execute_command("make", ['install'], self.get_install_path(), env)
    def _patch_timeout(self):
        """ Patch the cmake scripts to increase the timeout limit, geant4.9.5.p01 fix."""
        file_path = os.path.join(self._system.get_install_path(), 
                                 "%s-source/cmake/Modules/Geant4InstallData.cmake" % self._name)
        cmake_file = open(file_path, "r")
        text = cmake_file.read()
        cmake_file.close()
        text = text.replace("PREFIX", "TIMEOUT 10000\n        PREFIX")
        cmake_file = open(file_path, "w")
        cmake_file.write(text)
        cmake_file.close()
        
class Geant4Pre5(localpackage.LocalPackage):
    """ Base geant4 installer for pre 4.9.5 geant versions."""
    def __init__(self, name, system, tar_name, data_tars, clhep_dep, xerces_dep):
        """ Initialise the geant4 package."""
        super(Geant4Pre5, self).__init__(name, system)
        self._clhep_dep = clhep_dep
        self._data_tars = data_tars
        self._tar_name = tar_name
        self._xerces_dep = xerces_dep
    def get_dependencies(self):
        """ Return the dependency names as a list of names."""
        dependencies = ["make", "g++", "gcc", self._xerces_dep, self._clhep_dep]
        if self._system.get_install_mode() == installmode.Graphical:
            dependencies.extend(["Xm", "Xt", "opengl", "Xmu", "Xi"])
        return dependencies
    def _is_downloaded(self):
        """ Check tar files have been downloaded."""
        downloaded = True
        for tar in self._data_tars:
            downloaded = downloaded and self._system.file_exists(tar)
        downloaded = downloaded and self._system.file_exists(self._tar_name)
        return downloaded
    def _is_installed(self):
        """ Check geant has been installed."""
        sys = os.uname()[0] + "-g++"
        return self._system.library_exists("libG4event", 
                                           os.path.join(self.get_install_path(), "lib/" + sys)) and \
            self._system.library_exists("libG4UIbasic", 
                                        os.path.join(self.get_install_path(), "lib/" + sys))
    def _download(self):
        """ Derived classes should override this to download the package."""
        self._system.download_file(
            "http://geant4.web.cern.ch/geant4/support/source/" + self._tar_name)
        for tar in self._data_tars:
            self._system.download_file("http://geant4.web.cern.ch/geant4/support/source/" + tar)
    def _install(self):
        """ Derived classes should override this to install the package, should install only when 
        finished. Return True on success.
        """
        sys = os.uname()[0] + "-g++"
        self._system.untar_file(self._tar_name, self.get_install_path(), 1)
        for tar in self._data_tars:
            self._system.untar_file(tar, os.path.join(self.get_install_path(), "data"), 0)
        self.write_geant4_config_file()
        self._system.configure_command('./Configure', ['-incflags', '-build', '-d', '-e', 
                                                       '-f', "geant4-snoing-config.sh"], 
                                       cwd=self.get_install_path(), config_type="geant4")
        self._system.configure_command('./Configure', ['-incflags', '-install', '-d', '-e', 
                                                       '-f', "geant4-snoing-config.sh"], 
                                       cwd=self.get_install_path(), config_type="geant4")
        try:
            self._system.configure_command('./Configure', cwd=self.get_install_path(), config_type="geant4")
        except Exception: # Geant4 configure always fails, it is annoying
            pass
        if not os.path.exists(os.path.join(self.get_install_path(),'env.sh')):
            shutil.copy(os.path.join(self.get_install_path(), '.config/bin/' + sys + '/env.sh'), 
                        os.path.join(self.get_install_path(),'env.sh'))
            shutil.copy(os.path.join(self.get_install_path(), '.config/bin/' + sys + '/env.csh'), 
                        os.path.join(self.get_install_path(),'env.csh'))
    def write_geant4_config_file(self):
        """ Write the relevant geant4 configuration file, nasty function."""
        clhep_path = self._dependency_paths[self._clhep_dep]
        sys = os.uname()[0]
        config_text = "g4clhep_base_dir='%s'\ng4clhep_include_dir='%s'\ng4clhep_lib_dir='%s'\ng4data='%s'\ng4install='%s'\ng4osname='%s'\ng4system='%s'\n" % (clhep_path, os.path.join(clhep_path, "include"), os.path.join(clhep_path, "lib"), os.path.join(self.get_install_path(), "data"), self.get_install_path(), sys, sys + "-g++")
        config_text += "g4clhep_lib='CLHEP'\ng4compiler='g++'\ng4debug='n'\nd_portable='define'\ng4global='n'\ng4granular='y'\ng4include=''\ng4includes_flag='y'\ng4lib_build_shared='y'\ng4lib_build_static='y'\ng4lib_use_granular='y'\ng4lib_use_shared='n'\ng4lib_use_static='y'\ng4make='make'\ng4ui_build_gag_session='y'\ng4ui_build_terminal_session='y'\ng4ui_build_win32_session='n'\ng4ui_build_xaw_session='n'\ng4ui_use_gag='y'\ng4ui_use_tcsh='y'\ng4ui_use_terminal='y'\ng4ui_use_win32='n'\ng4ui_use_xaw='n'\ng4vis_build_oiwin32_driver='n'\ng4vis_build_oix_driver='n'\ng4vis_build_openglwin32_driver='n'\ng4vis_use_oiwin32='n'\ng4vis_use_oix='n'\ng4vis_use_openglwin32='n'\ng4w_use_g3tog4='n'\ng4wanalysis_build=''\ng4wanalysis_build_jas=''\ng4wanalysis_build_lab=''\ng4wanalysis_build_lizard=''\ng4wanalysis_use='n'\ng4wanalysis_use_jas=''\ng4wanalysis_use_lab=''\ng4wanalysis_use_lizard=''\ng4wlib_build_g3tog4='n'\n"
        xerces_path = self._dependency_paths[self._xerces_dep]
        if self._system.get_install_mode() == installmode.Graphical:
            config_text += "g4ui_build_xm_session='y'\ng4ui_use_xm='y'\ng4vis_build_asciitree_driver='y'\ng4vis_build_dawn_driver='y'\ng4vis_build_dawnfile_driver='y'\ng4vis_build_openglx_driver='y'\ng4vis_build_openglxm_driver='y'\ng4vis_build_raytracer_driver='y'\ng4vis_build_vrml_driver='y'\ng4vis_build_vrmlfile_driver='y'\ng4vis_oglhome='/usr'\noglhome='/usr'\ng4vis_use_asciitree='y'\ng4vis_use_dawn='y'\ng4vis_use_dawnfile='y'\ng4vis_use_openglx='y'\ng4vis_use_openglxm='y'\ng4vis_use_raytracer='y'\ng4vis_use_vrml='y'\ng4vis_use_vrmlfile='y'\ng4lib_build_gdml='y'\ng4gdml_xercesc_root='%s'\nwith_xercesc_root='%s'" % (xerces_path, xerces_path)
        else:
            config_text += "g4ui_build_xm_session='n'\ng4ui_use_xm='n'\ng4vis_build_asciitree_driver='n'\ng4vis_build_dawn_driver='n'\ng4vis_build_dawnfile_driver='n'\ng4vis_build_openglx_driver='n'\ng4vis_build_openglxm_driver='n'\ng4vis_build_raytracer_driver='n'\ng4vis_build_vrml_driver='n'\ng4vis_build_vrmlfile_driver='n'\ng4vis_oglhome=''\ng4vis_use_asciitree='n'\ng4vis_use_dawn='n'\ng4vis_use_dawnfile='n'\ng4vis_use_openglx='n'\ng4vis_use_openglxm='n'\ng4vis_use_raytracer='n'\ng4vis_use_vrml='n'\ng4vis_use_vrmlfile='n'\ng4vis_none='1'\ng4lib_build_gdml='y'\ng4gdml_xercesc_root='%s'\nwith_xercesc_root='%s'" % (xerces_path, xerces_path)
        configFile = open(os.path.join(self.get_install_path(), "geant4-snoing-config.sh"), "w")
        configFile.write(config_text)
        configFile.close()
