#!/usr/bin/env python
#
# Zeromq
#
# The zmq package installers, needed to send packed root events over the network.
#
# Author P G Jones - 19/05/2012 <p.g.jones@qmul.ac.uk> : First revision
# Author P G Jones - 22/09/2012 <p.g.jones@qmul.ac.uk> : Major refactor of snoing.
####################################################################################################
import conditionallibrarypackage
import os

class Zeromq(conditionallibrarypackage.ConditionalLibraryPackage):
    """ Zeromq install package."""
    def __init__(self, name, system, tar_name):
        """ Initlaise the ZMQ packages."""
        super(Zeromq, self).__init__(name, system, "zmq", ["zmq.h"])
        self._tar_name = tar_name
    def get_dependencies(self):
        """ Return the dependencies."""
        return []
    def _is_downloaded(self):
        """ Check if tar ball is downloaded."""
        return self._system.file_exists(self._tar_name)
    def _is_installed(self):
        return self._system.library_exists("libzmq", os.path.join(self.get_install_path(), "lib"))
    def _download(self):
        """ Download zmq."""
        self._download_pipe += self._system.download_file("http://download.zeromq.org/" + \
                                                              self._tar_name)
    def _install(self):
        """ Install zmq."""
        source_path = os.path.join(self._system.get_install_path(), "%s-source" % self._name)
        self._install_pipe += self._system.untar_file(self._tar_name, source_path, 1)
        self._install_pipe += self._system.execute_command("./configure", cwd=source_path)
        self._install_pipe += self._system.execute_command("make", cwd=source_path)
        self._install_pipe += self._system.execute_command("make", 
                                                           ["install", "prefix=%s" % self.get_install_path()], 
                                                           cwd=source_path)
