#!/usr/bin/env python
# Author P G Jones - 20/06/2012 <p.g.jones@qmul.ac.uk> : First revision
# Conditional library package, checks if installed on the system. If not installs locally e.g. curl.
import ConditionalPackage
import os
import PackageUtil
import Log

class ConditionalLibraryPackage( ConditionalPackage.ConditionalPackage ):
    """ Base class to install libraries."""
    def __init__( self, name, library, header = None ):
        """ Initialise the package, grab a lock."""
        super( ConditionalLibraryPackage, self ).__init__( name )
        self._Library = library
        self._Header = header
        return
    def CheckState( self ):
        """ Check if package is installed on the system first."""
        if PackageUtil.TestLibrary( self._Library, self._Header ):
            self._SetMode( 2 )
        else:
            self._InstallPath = os.path.join( PackageUtil.kInstallPath, self._Name ) # Use local install path
            self._CheckState()
        return
    # Functions to override
    def _CheckState( self ):
        """ Derived classes should override this to ascertain the package status, downloaded? installed?"""
        return
