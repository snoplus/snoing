#!/usr/bin/env python
# Author P G Jones - 19/05/2012 <p.g.jones@qmul.ac.uk> : First revision
# Package utility module, has many useful functions
import urllib2
import subprocess
import tarfile
import os
import shutil
import base64
import sys
from contextlib import closing

kCachePath = ""
kInstallPath = ""
kGraphical = False
kVerbose = False

def DownloadFile( url, username = None, password = None ): # Never hard code a password!
    """ Download a file at url, using the username and password if provided and save into the cachePath."""
    global kCachePath, kInstallPath, kVerbose
    fileName = url.split('/')[-1]
    urlRequest = urllib2.Request( url )
    if username != None: # Add simple HTTP authorization
        b64string = base64.encodestring( '%s:%s' % ( username, password ) ).replace( '\n', '' )
        urlRequest.add_header( "Authorization", "Basic %s" % b64string )
    with closing( urllib2.urlopen( urlRequest ) ) as remoteFile:
        with open( os.path.join( kCachePath, fileName ), 'wb') as localFile:
            downloadSize = int( remoteFile.info().getheaders("Content-Length")[0] )
            downloaded = 0 # Amount downloaded
            blockSize = 8192 # Convenient block size
            while True:
                buffer = remoteFile.read( blockSize )
                if not buffer: # Nothing left to download
                    break
                downloaded += len( buffer )
                localFile.write( buffer )
    if downloaded < downloadSize: # Something has gone wrong
        raise Exception( "Download error" )
    return "Downloaded %i bytes\n" % downloadSize
    
def ExecuteSimpleCommand( command, args, env, cwd ):
    """ Blocking execute command. Returns True on success"""
    global kCachePath, kInstallPath, kVerbose
    shellCommand = [ command ] + args
    process = subprocess.Popen( args = shellCommand, env = env, cwd = cwd, stdout = subprocess.PIPE )
    if kVerbose:
        for line in iter( process.stdout.readline, "" ):
            sys.stdout.write( '\n' + line[:-1] )
            sys.stdout.flush()
    output, error = process.communicate()
    if process.returncode <= 0:
        raise Exception( "Command Error" )
    return output

def ExecuteComplexCommand( command ):
    """ Execute a multiple line bash command, writes to a temp bash file then executes it."""
    global kCachePath, kInstallPath
    fileName = os.path.join( kInstallPath, "temp.sh" )
    with open( fileName, "w" ) as commandFile:
        commandFile.write( command )
    output = ExecuteSimpleCommand( "/bin/bash", [fileName], os.environ, kInstallPath )
    os.remove( fileName )
    return output

def UnTarFile( tarFileName, targetPath, strip = 0 ):
    """ Untar the file tarFile to targetPath take off the the first strip folders."""
    global kCachePath, kInstallPath
    if strip == 0: # Can untar directly into target
        with closing( tarfile.open( os.path.join( kCachePath, tarFileName ) ) ) as tarFile:
            tarFile.extractall( targetPath )
    else: # Must untar to temp then to target, note target cannot already exist!
        # First untar to a temp directory
        tempDirectory = os.path.join( kCachePath, "temp" )
        with closing( tarfile.open( os.path.join( kCachePath, tarFileName ) ) ) as tarFile:
            tarFile.extractall( tempDirectory )
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
    return "Extracted %s\n" % tarFileName

def FindLibrary( libName ):
    """ Check if the library exists in the standard library locations. Return location if it does if not return None."""
    global kCachePath, kInstallPath
    command = "whereis " + libName
    process = subprocess.Popen( args = command, shell = True, stdout=subprocess.PIPE)
    x, y = process.communicate()
    location = x.split( ':' )
    if location[1] == "\n":
        return None
    else:
        return location[1]

def TestLibrary( libName, header = None ):
    """ Test if code can be compiled with header and linked to libName."""
    global kCachePath, kInstallPath
    fileText = ""
    if header != None:
        fileText = "#include <%s>\n" % header
    fileText += "int main( int a, char* b[] ) { }"
    fileName = os.path.join( kInstallPath, "temp.cc" )
    with open( fileName, "w" ) as testFile:
        testFile.write( fileText )
    try:
        output = ExecuteSimpleCommand( "g++", [fileName, "-l", libName], os.environ, kInstallPath )
        os.remove( fileName )
        return True
    except Exception:
        os.remove( fileName )
        return False
