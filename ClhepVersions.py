#!/usr/bin/env python
# Author P G Jones - 13/05/2012 <p.g.jones@qmul.ac.uk> : First revision
# The CLHEP packages (versions)
import Clhep

class CLHEP2101( Clhep.Clhep ):
    """ Clhep 2.1.0.1, install package."""
    def __init__( self, cachePath, installPath, graphical ):
        """ Initiliase the clhep 2.1.0.1 package."""
        super( CLHEP2101, self ).__init__( "clhep-2.1.0.1", cachePath, installPath, "clhep-2.1.0.1.tgz" )
        return
    def _Download( self ):
        """ Derived classes should override this to download the package. Return True on success."""
        self._DownloadFile( "http://proj-clhep.web.cern.ch/proj-clhep/DISTRIBUTION/tarFiles/clhep-2.1.0.1.tgz" )
        return True

class CLHEP2042( Clhep.Clhep ):
    """ Clhep 2.0.4.2, install package."""
    def __init__( self, cachePath, installPath, graphical ):
        """ Initiliase the clhep 2.0.4.2 package."""
        super( CLHEP2042, self ).__init__( "clhep-2.0.4.2", cachePath, installPath, "clhep-2.0.4.2.tgz" )
        return
    def _Download( self ):
        """ Derived classes should override this to download the package. Return True on success."""
        self._DownloadFile( "http://proj-clhep.web.cern.ch/proj-clhep/DISTRIBUTION/distributions/clhep-2.0.4.2.tgz" )
        return True
