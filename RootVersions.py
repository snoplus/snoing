#!/usr/bin/env python
# Author P G Jones - 12/05/2012 <p.g.jones@qmul.ac.uk> : First revision
# Author P G Jones - 13/05/2012 <p.g.jones@qmul.ac.uk> : Added 5.32, 5.28, 5.24 versions (rat v3, v2, v1)
# The ROOT packages (versions)
import Root

class ROOT53203( Root.Root ):
    """ Root 5.32.03, install package."""
    def __init__( self, cachePath, installPath ):
        """ Initiliase the root 5.32.00 package."""
        super( ROOT53203, self ).__init__( "root-5.32.03", cachePath, installPath, "root_v5.32.03.source.tar.gz" )
        return
    def _Download( self ):
        """ Derived classes should override this to download the package. Return True on success."""
        self._DownloadFile( "ftp://root.cern.ch/root/root_v5.32.03.source.tar.gz" )
        return True

class ROOT52800( Root.Root ):
    """ Root 5.28.00, install package."""
    def __init__( self, cachePath, installPath ):
        """ Initiliase the root 5.32.00 package."""
        super( ROOT52800, self ).__init__( "root-5.28.00", cachePath, installPath, "root_v5.28.00h.source.tar.gz" )
        return
    def _Download( self ):
        """ Derived classes should override this to download the package. Return True on success."""
        self._DownloadFile( "ftp://root.cern.ch/root/root_v5.28.00h.source.tar.gz" )
        return True

class ROOT52400( Root.Root ):
    """ Root 5.24.00, install package."""
    def __init__( self, cachePath, installPath ):
        """ Initiliase the root 5.32.00 package."""
        super( ROOT52400, self ).__init__( "root-5.24.00", cachePath, installPath, "root_v5.24.00b.source.tar.gz" )
        return
    def _Download( self ):
        """ Derived classes should override this to download the package. Return True on success."""
        self._DownloadFile( "ftp://root.cern.ch/root/root_v5.24.00b.source.tar.gz" )
        return True
