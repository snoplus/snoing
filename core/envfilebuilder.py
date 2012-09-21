#!/usr/bin/env python
#
# EnvFileBuilder
#
# Writes out environment files in a correctly formated manner.
#
# Author P G Jones - 21/06/2012 <p.g.jones@qmul.ac.uk> : First revision
# Author P G Jones - 23/06/2012 <p.g.jones@qmul.ac.uk> : Major refactor of snoing.
####################################################################################################
import os

class EnvFileBuilder( object ):
    """ Builds the env files correctly."""
    def __init__(self, comment=None):
        """ Initialise the env file with an optional comment."""
        self._bash_text = "#!/bin/bash\n" # Full text for the bash file
        self._csh_text = "#!/bin/csh\n" # Full text for the csh file
        if comment:
            self._bash_text += comment
            self._csh_text += comment
        self._library_path = "" # Full library path environment text (additions)
        self._path = "" # Full path environment text (additions)
        self._python_path = "" # Full python path environment text (additions)
        self._bash_post_text = "" # Text to go at the end of the bash file
        self._csh_post_text = "" # Text to go at the end of the csh file
    def add_source(self, file_path, file_name):
        """ Add a source command."""
        self._bash_text += "source %s/%s.sh\n" % (file_path, file_name)
        self._csh_text += "source %s/%s.csh\n" % (file_path, file_name)
    def add_post_source(self, file_path, file_name):
        """ Add a source command to the end of the file."""
        self._bash_post_text += "source %s/%s.sh\n" % (file_path, file_name)
        self._csh_post_text += "source %s/%s.csh\n" % (file_path, file_name)
    def add_environment(self, key, value):
        """ Add an environment variable."""
        self._bash_text += "export %s=%s\n" % (key, value)
        self._csh_text += "setenv %s %s\n" % (key, value)
    def append_library_path(self, path):
        """ Append a path to the library path."""
        self._library_path += "%s:" % path
    def append_path(self, path):
        """ Append a path to the PATH."""
        self._path += "%s:" % path
    def append_python_path(self, path):
        """ Append a path to the PYTHPNPATH."""
        self._python_path += "%s:" % path
    def write(self, directory, name):
        """ Write the env files to the directory called name.sh and name.csh."""
        # Strip the trailing :
        self._library_path = self._library_path[0:-1]
        self._path = self._path[0:-1]
        self._python_path = self._python_path[0:-1]
        # First add the Path
        self._bash_text += "export PATH=%s:$PATH\n" % self._path
        self._csh_text += "setenv PATH %s:${PATH}\n" % self._path
        # Next add the python path
        self._bash_text += "export PYTHONPATH=%s:$PYTHONPATH\n" % self._python_path
        self._csh_text += ("if(${?PYTHONPATH}) then\nsetenv PYTHONPATH %s:${PYTHONPATH}\nelse\n"
                           "setenv PYTHONPATH %s\nendif\n") % (self._python_path, self._python_path)
        # Next add the libraries (Harder for cshell)
        self._bash_text += "export LD_LIBRARY_PATH=%s:$LD_LIBRARY_PATH\n" % self._library_path
        self._bash_text += "export DYLD_LIBRARY_PATH=%s:$DYLD_LIBRARY_PATH\n" % self._library_path
        self._csh_text += ("if(${?LD_LIBRARY_PATH}) then\nsetenv LD_LIBRARY_PATH %s:"
                           "${LD_LIBRARY_PATH}\nelse\nsetenv LD_LIBRARY_PATH %s\nendif\n") % \
                           (self._library_path, self._library_path)
        self._csh_text += ("if(${?DYLD_LIBRARY_PATH}) then\nsetenv DYLD_LIBRARY_PATH %s:"
                           "${DYLD_LIBRARY_PATH}\nelse\nsetenv DYLD_LIBRARY_PATH %s\nendif\n") % \
                           (self._library_path, self._library_path)
        # Finnally add the rat
        self._bash_text += self._bash_post_text
        self._csh_text += self._csh_post_text
        # Now write the files
        bash_file = open(os.path.join(directory, "%s.sh" % name), "w")
        bash_file.write(self._bash_text)
        bash_file.close()
        csh_file = open(os.path.join(directory, "%s.csh" % name), "w")
        csh_file.write(self._csh_text)
        csh_file.close()
