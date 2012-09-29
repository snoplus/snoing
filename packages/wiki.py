#!/usr/bin/env python
#
# Wiki
#
# Allows installing of a documentation wiki
#
# Author P G Jones - 29/09/2012 <p.g.jones@qmul.ac.uk> : First revision
####################################################################################################
import localpackage
import envfilebuilder
import os

class Wiki(localpackage.LocalPackage):
    """ Base class for all wiki installations."""
    def __init__(self, name, system, git_url):
        """ Initialise with the git_url."""
        super(Wiki, self).__init__(name, system)
        self._git_url = git_url
        self._env_file = envfilebuilder.EnvFileBuilder("#wiki environment\n")
    def get_dependencies(self):
        """ Return the required dependencies."""
        return ["git", "gollum"]
    def _is_downloaded( self ):
        """ Check if downloaded."""
        return True
    def _is_installed(self):
        """ Check if installed, look for library."""
        return self._system.file_exists("Home.md", self.get_install_path())
    def _download( self ):
        """ Nothing to do."""
        pass
    def _install(self):
        """ Install the wiki."""
        self._system.execute_command("git", ["clone %s" % self._git_url, self.get_install_path()])
        self._env_file.add_environment("GEM_PATH", self._dependency_paths["gollum"])
        self._env_file.append_path(os.path.join(self._dependency_paths["gollum"], "bin"))
        self._env_file.add_command("cd %s" % self.get_install_path())
        self._env_file.add_command("gollum")
        self._env_file.add_command("sleep 30")
        self._env_file.add_command("xdg-open http://localhost:4567")
        self._env_file.add_command("fg")
        self._env_file.write(self._system.get_install_path(), "env_%s" % self._name)
