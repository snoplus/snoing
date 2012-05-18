#!/usr/bin/env python
# Author P G Jones - 12/05/2012 <p.g.jones@qmul.ac.uk> : First revision
# Author P G Jones - 15/05/2012 <p.g.jones@qmul.ac.uk> : Restructure packages
# Package information base class, both local and system packages derive from this
import urllib2
import subprocess
import tarfile
import os
import shutil
import base64

class Package( object ):
    """ Base class to install libraries."""
    def __init__( self, name ):
        """ Construct the package with name"""
        self._Name = name
        self._InstallPath = None # Location where the package is installed
        return
    def GetName( self ):
        """ Return the package name."""
        return self._Name
    def GetInstallPath( self ):
        """ Return the package install location."""
        return self._InstallPath
    # Functions to override
    def CheckState( self ):
        """ Function to force the package to check what it's status is."""
        return
    def IsInstalled( self ):
        """ Check and return if package is installed."""
        return False
    # Useful functions (For Installing packages)
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
    def _ExecuteComplexCommand( self, command ):
        """ Execute a multiple line command, writes to a temp file then executes it."""
        fileName = os.path.join( self._InstallPath, "temp.sh" )
        commandFile = open( fileName, "w" )
        commandFile.write( command )
        commandFile.close()
        self._ExecuteSimpleCommand( "source", [fileName], None, self._InstallPath )
        os.remove( fileName )
    def _ExecuteSimpleCommand( self, command, args, env, cwd ):
        """ Blocking execute command. Returns True on success"""
        shellCommand = [ command ] + args
        print shellCommand
        process = subprocess.Popen( args = shellCommand, env = env, cwd = cwd )#, executable = "/bin/bash" ) # Ensure bash shell is used
        return process.wait() == 0 # Blocks and waits for command to finish
    def _UnTarFile( self, tarFileName, targetPath, strip = 0 ):
        """ Untar the file tarFile to targetPath."""
        # First untar to a temp directory
        tempDirectory = os.path.join( self._CachePath, "temp" )
        tarFile = tarfile.open( os.path.join( self._CachePath, tarFileName ) )
        tarFile.extractall( tempDirectory )
        tarFile.close()
        # Now choose how many components to strip
        copyDirectory = tempDirectory
        for iStrip in range( 0, strip ):
            subFolders = os.listdir( copyDirectory )
            copyDirectory = os.path.join( copyDirectory, subFolders[0] )
        # Now can copy, first make sure the targetPath does not exist
        if os.path.exists( targetPath ):
            shutil.rmtree( targetPath )
        # Now copy
        shutil.copytree( copyDirectory, targetPath )
        shutil.rmtree( tempDirectory )
        return True
    # Useful functions for ascertaining if packages exist
    def _FindLibrary( self, libName ):
        """ Check if the library exists in the standard library locations. Return location if it does if not return None."""
        command = "whereis " + libName
        process = subprocess.Popen( args = command, shell = True, stdout=subprocess.PIPE)
        x, y = process.communicate()
        location = x.split( ':' )
        if location[1] == "\n":
            return None
        else:
            return location[1]
    def _TestLibrary( self, libName, header ):
        """ Test if code can be compiled with header and linked to libName."""

        return False
