#!/usr/bin/env python
# Author P G Jones - 13/05/2012 <p.g.jones@qmul.ac.uk> : First revision
# Author P G Jones - 23/06/2012 <p.g.jones@qmul.ac.uk> : Refactor of Package Structure
# Takes care of packages that are simple commands such as make, assumes name is the command
import SystemPackage
import PackageUtil

class CommandPackage( SystemPackage.SystemPackage ):
    """ For packages that are simple commands such as make."""
    def __init__( self, name, helpText ):
        """ Initialise the package."""
        super( CommandPackage, self ).__init__( name, helpText )
        return
    def CheckState( self ):
        """ For a command package, merely need to test if the command exists."""
        if PackageUtil.FindLibrary( self._Name ) is not None:
            self._Installed = True
        return
