#!/usr/bin/env python
# Author P G Jones - 12/05/2012 <p.g.jones@qmul.ac.uk> : First revision
# The SCONS packages base class
import LocalPackage
import os
import PackageUtil
import stat

class Scons( LocalPackage.LocalPackage ):
    """ Base scons installer, different versions only have different names."""
    def __init__( self, name, cachePath, installPath, tarName ):
        """ Initialise the scons package."""
        super( Scons, self ).__init__( name, cachePath, installPath, False )
        self._InstallPath = os.path.join( self._InstallPath, name )
        self._TarName = tarName
        return
    # Functions to override
    def CheckState( self ):
        """ Derived classes should override this to ascertain the package status, downloaded? installed?"""
        if os.path.exists( os.path.join( self._CachePath, self._TarName ) ):
            self._SetMode( 1 ) # Downloaded 
        if os.path.exists( os.path.join( self.GetInstallPath(), "script/scons" ) ) and \
                bool( os.stat( os.path.join( self.GetInstallPath(), "script/scons" ) ).st_mode & stat.S_IXUSR ):
            self._SetMode( 2 ) # Installed as well
        return
    def GetDependencies( self ):
        """ Return the dependency names as a list of names."""
        return []
    def _Install( self ):
        """ Derived classes should override this to install the package, should install only when finished. Return True on success."""
        result = PackageUtil.UnTarFile( self._TarName, self.GetInstallPath(), 1 )
        os.chmod( os.path.join( self.GetInstallPath(), "script/scons" ), 0751 )
        return result
