#!/usr/bin/env python
# Author P G Jones - 21/06/2012 <p.g.jones@qmul.ac.uk> : First revision
# Produces the RAT environment files both bash and csh
import os
import PackageUtil

class EnvFileBuilder( object ):
    """ Builds the env file for rat."""
    def __init__( self ):
        """ Initialise the env file text."""
        self._BashEnv = "#!/bin/bash\n#ratcage environment\n"
        self._CshEnv = "#!/bin/csh\n#ratcage environment\n"
        self._LibraryPath = ""
        self._Path = ""
        self._PythonPath = ""
        self._RatEnv = ""
        return
    def AddGeant( self, envFilePath, envFileName ):
        """ Add the geant environment file path to the env script."""
        self._BashEnv += "source %s/%s.sh\n" % ( envFilePath, envFileName )
        self._CshEnv += "source %s/%s.csh\n" % ( envFilePath, envFileName )
        return
    def AddEnvironment( self, key, value ):
        """ Add an environment variable."""
        self._BashEnv += "export %s=%s\n" % ( key, value )
        self._CshEnv += "setenv %s %s\n" % ( key, value )
        return
    def AppendLibraryPath( self, path ):
        """ Append a path to the library paths."""
        self._LibraryPath += "%s:" % path
        return
    def AppendPath( self, path ):
        """ Append a path to the PATH."""
        self._Path += "%s:" % path
        return
    def AppendPythonPath( self, path ):
        """ Append a path to the PYTHPNPATH."""
        self._PythonPath += "%s:" % path
        return
    def AddRat( self, path ):
        """ Set the path to the env file, almost always RATROOT."""
        self._RatEnv = path
        return
    def WriteEnvFiles( self, directory, name ):
        """ Write the env files to the directory."""
        # First add the Path
        self._BashEnv += "export PATH=%s$PATH\n" % self._Path
        self._CshEnv += "setenv PATH %s${PATH}\n" % self._Path
        # Next add the python path
        self._BashEnv += "export PYTHONPATH=%s$PYTHONPATH\n" % self._PythonPath
        self._CshEnv += "setenv PYTHONPATH %s${PYTHONPATH}\n" % self._PythonPath
        # Next add the libraries (Harder for cshell)
        self._BashEnv += "export LD_LIBRARY_PATH=%s$LD_LIBRARY_PATH\n" % self._LibraryPath
        self._BashEnv += "export DYLD_LIBRARY_PATH=%s$DYLD_LIBRARY_PATH\n" % self._LibraryPath
        self._CshEnv += "if(${?LD_LIBRARY_PATH}) then\nsetenv LD_LIBRARY_PATH %s${LD_LIBRARY_PATH}\nelse\nsetenv LD_LIBRARY_PATH %s\n" % ( self._LibraryPath, self._LibraryPath )
        self._CshEnv += "if(${?DYLD_LIBRARY_PATH}) then\nsetenv DYLD_LIBRARY_PATH %s${DYLD_LIBRARY_PATH}\nelse\nsetenv DYLD_LIBRARY_PATH %s\n" % (self._LibraryPath, self._LibraryPath )
        # Finnally add the rat
        self._BashEnv += "source %s/env.sh" % self._RatEnv
        self._CshEnv += "source %s/env.csh" % self._RatEnv
        # Now write the files
        bashFile = open( os.path.join( directory, "env_%s.sh" % name ), "w" )
        bashFile.write( self._BashEnv )
        bashFile.close()
        cshFile = open( os.path.join( directory, "env_%s.csh" % name ), "w" )
        cshFile.write( self._BashEnv )
        cshFile.close()
        return
