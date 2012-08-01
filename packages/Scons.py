#!/usr/bin/env python
# Author P G Jones - 12/05/2012 <p.g.jones@qmul.ac.uk> : First revision
# The SCONS packages base class
import LocalPackage
import os
import PackageUtil
import stat

class Scons( LocalPackage.LocalPackage ):
    """ Base scons installer, different versions only have different names."""
    def __init__( self, name, tarName ):
        """ Initialise the scons package."""
        super( Scons, self ).__init__( name )
        self._TarName = tarName
        return
    # Functions to override
    def GetDependencies( self ):
        """ Return the dependency names as a list of names."""
        return ["python"]
    def _IsDownloaded( self ):
        """ Check the tar ball has been downloaded."""
        return os.path.exists( os.path.join( PackageUtil.kCachePath, self._TarName ) )
    def _IsInstalled( self ):
        """ Check the script has been marked as executable."""
        return os.path.exists( os.path.join( self.GetInstallPath(), "script/scons" ) ) and \
            bool( os.stat( os.path.join( self.GetInstallPath(), "script/scons" ) ).st_mode & stat.S_IXUSR )
    def _Download( self ):
        """ Depends on the version."""
        pass
    def _Install( self ):
        """ Mark the script as executable."""
        self._InstallPipe += PackageUtil.UnTarFile( self._TarName, self.GetInstallPath(), 1 )
        os.chmod( os.path.join( self.GetInstallPath(), "script/scons" ), 0755 )
        return
