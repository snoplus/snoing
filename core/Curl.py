#!/usr/bin/env python
# Author O. Wasalski - 04/06/2012 <wasalski@berkeley.edu> : First revision, new file
import os
import PackageUtil
import ConditionalPackage

class Curl( ConditionalPackage.ConditionalPackage ):
    """ 
    Base curl installer package.
    Because of problems with curl's makefile, the package is
    installed in a sub-directory of the untarred package
    in the install/curl-$VERSION/install directory.
    """
    def __init__( self, name ):
        super( Curl, self ).__init__( name, "curl", "curl/curl.h" )

############ "Public" functions - overrides ConditionalPackage ############
    def GetInstallPath( self ):
        """ 
        Overrides the get install path function from the ConditionalPackage 
        class to facilitate curl being installed in a subdirectory.  
        """
        return os.path.join( self._GetSourcePath(), "install" )

########### "Private" functions - overrides ConditionalPackage ############
    def _Download( self ):
        """ 
        Downloads a curl tarball from the curl website.
        Should I be downloading dev version from github instead????
        """
        filename = "http://curl.haxx.se/download/%s.tar.gz" %( self._Name )
        result, self._DownloadPipe = PackageUtil.DownloadFile( filename )
        return result

    def _Install( self ):
        """ Returns true on success. """
        env = os.environ
        sourcePath = self._GetSourcePath()
        installPath = self.GetInstallPath()

        self._InstallPipe += PackageUtil.UnTarFile( "%s.tar.gz" %( self._Name ), sourcePath, 1 )
        os.mkdir( installPath )
        self._InstallPipe += PackageUtil.ExecuteSimpleCommand( "./configure", [ "--prefix=%s" %( installPath ) ], env, sourcePath )
        self._InstallPipe += PackageUtil.ExecuteSimpleCommand( "make", [], env, sourcePath )
        self._InstallPipe += PackageUtil.ExecuteSimpleCommand( "make", [ "install" ], env, sourcePath )
        return True

    def _CheckState( self ):
        """ Ascertains the package status by checking for certain files. """
        if self._TestDownloaded():
            if self._TestInstalled():
                self._SetMode( 2 )
            else:
                self._SetMode( 1 )
        else:
            self._SetMode( 0 )

############ "Private" functions - helper for this class only #############
    def _GetSourcePath( self ):
        """ Returns the path of the source code. """
        return os.path.join( PackageUtil.kInstallPath, self._Name )

    def _TestDownloaded( self ):
        """ Returns true if the curl.h file is in the proper directory. """
        return os.path.isfile( \
            os.path.join( \
                self._GetSourcePath(), "include", "curl", "curl.h" ) )

    def _TestInstalled( self ):
        """ 
        Returns true if the header, library and binary files are
        in the proper location.
        """
        installPath = self.GetInstallPath()
        header = os.path.isfile( \
            os.path.join( installPath, "include", "curl", "curl.h" ) )
        lib = os.path.isfile( os.path.join( installPath, "lib", "libcurl.a" ) )
        bin = os.path.isfile( os.path.join( installPath, "bin", "curl" ) )
        config = os.path.isfile( \
            os.path.join( installPath, "bin", "curl-config" ) )
        return header and lib and bin and config
        
