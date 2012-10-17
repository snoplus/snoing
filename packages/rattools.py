#!/usr/bin/env python
#
# RatTools
#
# Git clones rat-tools and installs the various sub projects
#
# Author P G Jones - 15/10/2012 <p.g.jones@qmul.ac.uk> : First revision
####################################################################################################
import localpackage
import os
import system

class RatTools(localpackage.LocalPackage):
    """ Base class for rat-tools."""
    def __init__(self, name, system, root_dep):
        """ Initialise rat-tools."""
        self._root_dep = root_dep
        super(RatTools, self).__init__(name, system)
    def get_dependencies(self):
        """ Depends on rat-dev and root."""
        return ["rat-dev", self._root_dep]
    def _is_downloaded(self):
        """ Check if downloaded."""
        return os.path.exists(self.get_install_path())
    def _is_installed(self):
        """ RATZDAB wont install on macs."""
        if self._system.get_os_type == system.System.Mac:
            return self._system.file_exists('README.md',os.path.join(self.get_install_path(),'README.md'))
        else:
            return self._system.file_exists('zdab2root',os.path.join(self.get_install_path(),
                                                                     os.path.join('ratzdab','bin')))
    def _download(self):
        """ Git clone rat-dev."""
        self._system.execute_command("git", ["clone", "git@github.com:snoplus/rat-tools.git",
                                             self.get_install_path()],
                                     verbose=True)
    def _install(self):
        """ Install RATZDAB, except on macs."""
        env = {"RATROOT" : self._dependency_paths["rat-dev"],
               "ROOTSYS" : self._dependency_paths[self._root_dep]}
        ratzdab_path = os.path.join(self.get_install_path(), "ratzdab")
        if self._system.get_os_type() == system.System.Mac:
            return
        self._system.execute_command("make", [], ratzdab_path, env)
    def _update(self):
        """ Special updater for rat-tools, just git pull then install again."""
        self._system.execute_command("git", ["pull"], cwd=self.get_install_path(), verbose=True)
        self._install()
