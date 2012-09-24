#!/usr/bin/env python
#
# Avalanche, AvalancheRelease
#
# Deals with network sending and recieving of SNO+ events.
#
# Author P G Jones - 16/05/2012 <p.g.jones@qmul.ac.uk> : First revision
#        O Wasalski - 05/06/2012 <wasalski@berkeley.edu> : Added curl dependency
#        P G Jones - 11/07/2012 <p.g.jones@qmul.ac.uk> : Refactor into dev and fixed versions
# Author P G Jones - 22/09/2012 <p.g.jones@qmul.ac.uk> : Major refactor of snoing.
####################################################################################################
import localpackage
import os

class Avalanche(localpackage.LocalPackage):
    """ Base class for all Avalanche installations."""
    def __init__(self, name, system, zeromq_dep, root_dep, curl_dep, tar_name):
        """ Initialise with the zmq, root and curl dependency versions."""
        super(Avalanche, self).__init__(name, system)
        self._zeromq_dep = zeromq_dep
        self._root_dep = root_dep
        self._curl_dep = curl_dep
        self._lib_path = os.path.join(self.get_install_path(), "lib/cpp")
        self._tar_name = tar_name
    def get_dependencies(self):
        """ Return the required dependencies."""
        return [self._zeromq_dep, self._root_dep, self._curl_dep]
    def _is_downloaded( self ):
        """ Check if downloaded."""
        return self._system.file_exists(self._tar_name)
    def _is_installed(self):
        """ Check if installed, look for library."""
        return self._system.library_exists("libavalanche", self._lib_path)
    def _download( self ):
        """ Download avalanche release."""
        self._system.download_file("https://github.com/mastbaum/avalanche/tarball/" \
                                                             + self._tar_name)
    def _install(self):
        """ Install Avalanche."""
        self._system.untar_file(self._tar_name, self.get_install_path(), 1)
        env = {"PATH" : os.path.join(self._dependency_paths[self._root_dep], "bin"),
               "ROOTSYS" : self._dependency_paths[self._root_dep]}
        args = ["CXXFLAGS=-L%s/lib -I%s/include -L%s/lib -I%s/include" % \
                    (self._dependency_paths[self._zeromq_dep], self._dependency_paths[self._zeromq_dep],
                     self._dependency_paths[self._curl_dep], self._dependency_paths[self._curl_dep]) ]
        self._system.execute_command("make", args, self._lib_path, env)
