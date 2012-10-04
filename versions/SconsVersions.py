#!/usr/bin/env python
# Author P G Jones - 13/05/2012 <p.g.jones@qmul.ac.uk> : First revision
# The SCONS packages (versions)
import Scons
import PackageUtil

class SCONS210( Scons.Scons ):
    """ Scons 2.1.0, install package."""
    def __init__( self ):
        """ Initiliase the scons 2.1.0 package."""
        super( SCONS210, self ).__init__( "scons-2.1.0", "scons-2.1.0.tar.gz" )
        return
    def _Download( self ):
        """ Derived classes should override this to download the package."""
        self._DownloadPipe += PackageUtil.DownloadFile( "http://downloads.sourceforge.net/project/scons/scons/2.1.0/scons-2.1.0.tar.gz" )
        return

class SCONS120( Scons.Scons ):
    """ Scons 1.2.0, install package."""
    def __init__( self ):
        """ Initiliase the scons 1.2.0 package."""
        super( SCONS120, self ).__init__( "scons-1.2.0", "scons-1.2.0.tar.gz" )
        return
    def _Download( self ):
        """ Derived classes should override this to download the package."""
        self._DownloadPipe += PackageUtil.DownloadFile( "http://downloads.sourceforge.net/project/scons/scons/1.2.0/scons-1.2.0.tar.gz" )
        return
