#!/usr/bin/env python
# Author P G Jones - 23/06/2012 <p.g.jones@qmul.ac.uk> : First Revision
# Packages that cannot be installed, but should be present on the system
import Package

class SystemPackage( Package.Package ):
    """ Base class for system wide packages."""
    def __init__( self, name, helpText ):
        """ Construct the package with help text (which should be a hint to the user about what to install)."""
        super( SystemPackage, self ).__init__( name )
        self._HelpText = helpText
        self._Installed = False
        return
    def GetHelpText( self ):
        """ Return the package help text."""
        return self._HelpText
    def IsInstalled( self ):
        """ Check and return if package is installed."""
        return self._Installed
    # Functions to override by sublasses
    def CheckState( self ):
        """ Function to force the package to check what it's status is."""
        pass
