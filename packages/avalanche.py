#!/usr/bin/env python
#
# Avalanche
#
# Git clones avalanche and installs it
#
# Author P G Jones - 17/10/2012 <p.g.jones@qmul.ac.uk> : First revision
####################################################################################################
import localpackage
import os

class Avalanche(localpackage.LocalPackage):
    """ Base class for avalanche."""
    def __init__(self, name, system, root_dep, curl_dep):
        """ Initialise avalanche."""
        self._root_dep = root_dep
        self._curl_dep = curl_dep
        super(Avalanche, self).__init__(name, system)
    def get_dependencies(self):
        """ Depends on rat-dev and root."""
        return ["rat-dev", "rattools-dev", self._root_dep, self._curl_dep]
    def _is_downloaded(self):
        """ Check if downloaded."""
        return os.path.exists(self.get_install_path())
    def _is_installed(self):
        return self._system.library_exists("libavalanche", os.path.join(self.get_install_path(), 
                                                                        "lib"))
    def _download(self):
        """ Git clone rat-dev."""
        self._system.execute_command("git", ["clone", "git@github.com:pgjones/avalanche.git", # Switch back to mastbaum soon...
                                             self.get_install_path()],
                                     verbose=True)
    def _install(self):
        """ Install Avalanche."""
        env = {"RATROOT" : self._dependency_paths["rat-dev"],
               "ROOTSYS" : self._dependency_paths[self._root_dep],
               "RATZDAB_ROOT" : os.path.join(self._dependency_paths["rattools-dev"], "ratzdab"),
               "PATH" : os.path.join(self._dependency_paths[self._root_dep], "bin"),
               "LD_LIBRARY_PATH" : os.path.join(self._dependency_paths[self._root_dep], "lib")}
        if self._dependency_paths[self._curl_dep] is not None: # Conditional package
            env["PATH"] += ":" + os.path.join(self._dependency_paths[self._curl_dep], "bin")
            env["LD_LIBRARY_PATH"] += ":" + os.path.join(self._dependency_paths[self._curl_dep], "lib")
        self._system.execute_command("make", [], self.get_install_path(), env=env)
    def _update(self):
        """ Special updater for rat-tools, just git pull then install again."""
        self._system.execute_command("git", ["pull"], cwd=self.get_install_path(), verbose=True)
        self._install()

class AvalancheOld(localpackage.LocalPackage):
    """ Base class for old style release versions."""
    def __init__(self, name, system, zmq_dep, root_dep, curl_dep, tar_name):
        """ Initialise avalanche with the tarName."""
        super(AvalancheOld, self).__init__(name, system)
        self._tar_name = tar_name
        self._zeromq_dep = zmq_dep
        self._root_dep = root_dep
        self._curl_dep = curl_dep
    def get_dependencies( self ):
        """ Return the required dependencies."""
        return [self._zeromq_dep, self._root_dep, self._curl_dep]
    def _is_installed( self ):
        """ Check if installed."""
        return self._system.library_exists("libavalanche", 
                                           os.path.join(self.get_install_path(), "lib/cpp"))
    def _is_downloaded( self ):
        """ Check if downloaded."""
        return self._system.file_exists(self._tar_name)
    def _download( self ):
        """ Download avalanche (git clone)."""
        self._system.download_file("https://github.com/mastbaum/avalanche/tarball/" + self._tar_name)
    def _install( self ):
        """ Untar then call base installer."""
        self._system.untar_file(self._tar_name, self.get_install_path(), 1)
        env = {"PATH" : os.path.join(self._dependency_paths[self._root_dep], "bin"),
               "ROOTSYS" : self._dependency_paths[self._root_dep]}
        curl = self._dependency_paths[self._curl_dep] # Shorten the text
        zmq = self._dependency_paths[self._zeromq_dep] # Shorten the text
        self._system.execute_command("make", 
                                     ['CXXFLAGS=-L%s/lib -I%s/include -L%s/lib -I%s/include' % 
                                      (zmq, zmq, curl, curl)],
                                     cwd=os.path.join(self.get_install_path(), "lib/cpp"),
                                     env=env)
