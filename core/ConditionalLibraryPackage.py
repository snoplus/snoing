#!/usr/bin/env python
# Author P G Jones - 20/06/2012 <p.g.jones@qmul.ac.uk> : First revision
# Author P G Jones - 23/06/2012 <p.g.jones@qmul.ac.uk> : Refactor of Package Structure
# Conditional library package, checks if installed on the system. If not installs locally e.g. curl.
import ConditionalPackage
import PackageUtil

class ConditionalLibraryPackage( ConditionalPackage.ConditionalPackage ):
    """ Base class to install libraries."""
    def __init__( self, name, library, header = None ):
        """ Initialise the package, grab a lock."""
        super( ConditionalLibraryPackage, self ).__init__( name )
        self._Library = library
        self._Header = header
        return
    def _IsSytemInstalled( self ):
        """ Check if package is installed on the system first."""
        return PackageUtil.TestLibrary( self._Library, self._Header )
    # Functions to override
    def GetDependencies( self ):
        """ Return the dependency names as a list of names."""
        pass
    def _IsDownloaded( self ):
        """ Check if package is downloaded."""
        return False
    def _IsInstalled( self ):
        """ Check if package is installed."""
        return False
    def _Download( self ):
        """ Derived classes should override this to download the package.."""
        pass
    def _Install( self ):
        """ Derived classes should override this to install the package, should install only when finished."""
        pass
