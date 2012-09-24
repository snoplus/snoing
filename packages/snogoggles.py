#!/usr/bin/env python
#
# Snogoggles
#
# The snogoggles install packages.
#
# Author P G Jones - 24/06/2012 <p.g.jones@qmul.ac.uk> : First revision
# Author P G Jones - 27/07/2012 <p.g.jones@qmul.ac.uk> : Added snogoggles versions.
# Author P G Jones - 27/07/2012 <p.g.jones@qmul.ac.uk> : Moved to env file builder.
# Author P G Jones - 24/09/2012 <p.g.jones@qmul.ac.uk> : Major refactor of snoing.
####################################################################################################
import localpackage
import installmode
import os
import envfilebuilder

class Snogoggles(localpackage.LocalPackage):
    """ Base snogoggles installer for snogoggles."""
    def __init__(self, name, system, scons_dep, geant4_dep, clhep_dep, rat_dep, root_dep, \
                      sfml_dep, xercesc_dep, avalanche_dep, zmq_dep, curl_dep, bzip_dep):
        """ Initialise snogoggles."""
        super(Snogoggles, self).__init__(name, system)
        self.set_install_mode(installmode.Graphical) # Only graphical installation
        self._scons_dep = scons_dep
        self._geant_dep = geant4_dep
        self._clhep_dep = clhep_dep
        self._rat_dep = rat_dep
        self._root_dep = root_dep
        self._sfml_dep = sfml_dep
        self._xercesc_dep = xercesc_dep
        self._avalanche_dep = avalanche_dep
        self._zeromq_dep = zmq_dep
        self._curl_dep = curl_dep
        self._bzip_dep = bzip_dep
        self._env_file = EnvFileBuilder.EnvFileBuilder("#snogoggles environment\n")
    def get_dependencies(self):
        """ Return the required dependencies."""
        dependencies = ["python", "python-dev", self._scons_dep, self._geant_dep, self._clhep_dep, self._rat_dep, \
                            self._root_dep, self._sfml_dep, self._xercesc_dep, self._avalanche_dep, \
                            self._zeromq_dep, self._curl_dep, self._bzip_dep]
        return dependencies
    def _is_downloaded( self ):
        """ Check if downloaded."""
        return os.path.exists( self.GetInstallPath() )
    def _is_installed(self):
        """ Check if installed."""
        return self._system.file_exists("snogoggles", os.path.join(self.get_install_path(), "bin"))
    def _download( self ):
        """ Download snogoggles (git clone)."""
        self._system.execute_command( "git", ["clone", "git@github.com:snoplus/snogoggles.git",  
                                              self.get_install_path()], cwd=os.getcwd(), verbose=True)
    def _install(self):
        """ Install Snogoggles."""
        self.write_env_file()
        self._system.execute_complex_command("source env_%s.sh\ncd %s\nscons" % (self._Name, self.get_install_path()))
    def _update(self):
        """ Special updater for rat-dev, delete env file write a new then git pull and scons."""
        self._remove()
        self.write_env_file()
        command_text = "#!/bin/bash\nsource %s\ncd %s\ngit pull\nscons -c\nscons" % \
            (os.path.join(self._system.get_install_path(), "env_%s.sh" % self._name ), self.get_install_path())
        self._system.execute_complex_command(command_text, verbose=True)
    def _remove(self):
        """ Delete the env files as well."""
        os.remove(os.path.join(self._system.get_install_path(), "env_%s.sh" % self._name))
        os.remove(os.path.join(self._system.get_install_path(), "env_%s.csh" % self._name))
    def write_env_file(self):
        """ Adds general parts and then writes the env file."""
        self._EnvFile.add_source(self._dependency_paths[self._geant_dep], "bin/geant4")
        self._EnvFile.add_source(self._dependency_paths[self._rat_dep], "env")

        self._env_file.add_environment("VIEWERROOT", self.get_install_path())
        self._env_file.add_environment("ROOTSYS", self._dependency_paths[self._root_dep])
        self._env_file.add_environment("SFMLROOT", self._dependency_paths[self._sfml_dep])
        self._env_file.add_environment("GLEWROOT", os.path.join(self._dependency_paths[self._sfml_dep], "extlibs"))
        self._env_file.add_environment("AVALANCHEROOT", self._dependency_paths[self._avalanche_dep])
        if self._dependency_paths[self._zeromq_dep] is not None: # Conditional Package
            self._env_file.add_environment("ZEROMQROOT", self._dependency_paths[self._zeromq_dep])
        if self._dependency_paths[self._xercesc_dep] is not None: # Conditional Package
            self._env_file.add_environment("XERCESCROOT", self._dependency_paths[self._xercesc_dep])
        if self._dependency_paths[self._bzip_dep] is not None:
            self._env_file.add_environment("BZIPROOT", self._dependency_paths[self._bzip_dep])

        if self._dependency_paths[self._curl_dep] is not None:
            self._env_file.append_path(os.path.join(self._dependency_paths[self._curl_dep], "bin"))
        self._env_file.append_path(os.path.join(self.get_install_path(), "bin"))
        self._env_file.append_path(os.path.join(self._dependency_paths[self._root_dep], "bin"))
        self._env_file.append_path(os.path.join(self._dependency_paths[self._clhep_dep], "bin"))
        self._env_file.append_path(os.path.join(self._dependency_paths[self._scons_dep], "script"))

        self._env_file.append_python_path(os.path.join(self.get_install_path(), "python"))

        # Library path is always after the environment exports/setenvs
        self._env_file.append_library_path(os.path.join(self._dependency_paths[self._clhep_dep], "lib"))
        self._env_file.append_library_path("$ROOTSYS/lib:$AVALANCHEROOT/lib/cpp:$ZEROMQROOT/lib:$SFMLROOT/lib:$XERCESCROOT/lib:$GLEWROOT/lib")
        self._env_file.write(PackageUtil.kInstallPath, "env_%s" % self._name)
