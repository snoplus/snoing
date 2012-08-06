#!/usr/bin/env python
# Author P G Jones - 11/07/2012 <p.g.jones@qmul.ac.uk> : First revision
# The Xm library is special
import SystemPackage
import PackageUtil
import os

class Xm( SystemPackage.SystemPackage ):
    """ Package for the Open Motif/Xm library."""
    def __init__( self ):
        super( Xm, self ).__init__( "Xm", "Install Xm-dev (OpenMotif) on this system." )
        return
    def CheckState( self ):
        """ Check the Xm state, slightly more involved on macs."""
        sys =  os.uname()[0]
        if sys == 'Darwin':
            flags = []
            if os.path.exists( "/sw/include/Xm" ):
                flags = [ "-I%s" % "/sw/include/Xm", "-L%s" % "/sw/lib" ]
            elif os.path.exists( "/usr/OpenMotif" ):
                flags = [ "-I%s" % "/usr/OpenMotif/include", "-L%s" % "/usr/OpenMotif/lib" ]
            installed, self._CheckPipe = PackageUtil._TestLibrary( "Xm.h", flags )
            self._Installed = installed
        else:
            installed, self._CheckPipe = PackageUtil.TestLibrary( "Xm", "Xm/Xm.h" )
            self._Installed = installed
        return
