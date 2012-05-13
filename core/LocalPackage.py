#!/usr/bin/env python
# Author P G Jones - 12/05/2012 <p.g.jones@qmul.ac.uk> : First revision
# Package installer base class
import Package
import subprocess
import urllib2
import subprocess
import os
import tarfile

class LocalPackage( Package.Package ):
    """ Base class to install libraries."""
    def __init__( self, name, cachePath, installPath ):
        """ Initialise the package, grab a lock."""
        self._Mode = 0 # Mode 0 is initial, 1 is post download, 2 is post install
        self._Name = name
        self._CachePath = cachePath
        self._InstallPath = installPath
        self._DependencyPaths = {}
        return
    def IsDownloaded( self ):
        """ Return package is downloaded."""
        return self._Mode > 0
    def IsInstalled( self ):
        """ Check and return if package is installed."""
        return self._Mode > 1
    def SetDependencyPaths( self, paths ):
        """ Set the dependency path dictionary."""
        self._DependencyPaths = paths
        return
    def Install( self ):
        """ Full install process."""
        self.CheckState()
        self.Download()
        if not self.IsInstalled():
            if self._Install():
                self._IncrementMode()
            else:
                raise Exception( "Install error" )        
    def Download( self ):
        """ Full download process."""
        self.CheckState()
        if not self.IsDownloaded():
            if self._Download():
                self._IncrementMode()
            else:
                raise Exception( "Download error" )
        return
    # Functions to override
    def CheckState( self ):
        """ Derived classes should override this to ascertain the package status, downloaded? installed?"""
        return
    def GetDependencies( self ):
        """ Return the dependency names as a list of names."""
        return []
    def _Download( self ):
        """ Derived classes should override this to download the package. Return True on success."""
        return False
    def _Install( self ):
        """ Derived classes should override this to install the package, should install only when finished. Return True on success."""
        return False
    # Useful functions
    def _DownloadFile( self, url, username = None, password = None ): # Never hard code a password!
        """ Download the file at url, and place into cache. Returns True on success"""
        fileName = url.split('/')[-1]
        urlRequest = urllib2.Request( url )
        if username != None: # Add simple HTTP authorization
            b64string = base64.encodestring( '%s:%s' % ( username, password ) ).replace( '\n', '' )
            urlRequest.add_header( "Authorization", "Basic %s" % b64string )
        remoteFile = urllib2.urlopen( urlRequest )
        localFile = open( os.path.join( self._CachePath, fileName ), 'wb')
        downloadSize = int( remoteFile.info().getheaders("Content-Length")[0] )
        print "Downloading: %s Bytes: %s" % ( fileName, downloadSize )
        
        downloaded = 0 # Amount downloaded
        blockSize = 8192 # Convenient block size
        while True:
            buffer = remoteFile.read( blockSize )
            if not buffer: # Nothing left to download
                break
            
            downloaded += len( buffer )
            localFile.write( buffer )
            if downloaded != 0:
                print downloaded, downloadSize 
        localFile.close()
        return
    def _ExecuteCommand( self, command, args, env, cwd ):
        """ Blocking execute command. Returns True on success"""
        shellCommand = [ command ] + args
        print shellCommand
        process = subprocess.Popen( args = shellCommand, shell = True, env = env, cwd = cwd, executable = "/bin/bash" ) # Ensure bash shell is used
        return process.wait() == 0 # Blocks and waits for command to finish
    def _UnTarFile( self, tarFileName, path ):
        """ Untar the file tarFile to path."""
        tarFile = tarfile.open( os.path.join( self._CachePath, tarFileName ) )
        tarFile.extractall( path )
        tarFile.close()
        return
    def _IncrementMode( self ):
        """ Function to safely update the mode."""
        self._Mode += 1
        return
    def _SetMode( self, mode ):
        """ Function to safely set the mode."""
        self._Mode = mode
        return
