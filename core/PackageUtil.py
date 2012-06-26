#!/usr/bin/env python
# Author P G Jones - 19/05/2012 <p.g.jones@qmul.ac.uk> : First revision
#        OW - 07/06/2012 <wasalski@berkeley.edu> : Added optional filename to DownloadedFile function
# Package utility module, has many useful functions
import PackageException
import urllib2
import subprocess
import tarfile
import os
import shutil
import base64
import sys

kCachePath = ""
kInstallPath = ""
kGraphical = False
kVerbose = False

def DownloadFile( url, username = None, password = None, fileName = "" ): # Never hard code a password!
    """ Download a file at url, using the username and password if provided and save into the cachePath. Optional fileName parameter to manually name the file which gets stored in the cachePath"""
    global kCachePath, kInstallPath, kVerbose
    if( fileName == "" ): # OW 07/06/2012
        fileName = url.split('/')[-1]
    tempFile = os.path.join( kCachePath, "download-temp" )
    urlRequest = urllib2.Request( url )
    if username != None: # Add simple HTTP authorization
        b64string = base64.encodestring( '%s:%s' % ( username, password ) ).replace( '\n', '' )
        urlRequest.add_header( "Authorization", "Basic %s" % b64string )
    try:
        remoteFile = urllib2.urlopen( urlRequest )
    except urllib2.URLError: # Server not available
        raise PackageException.PackageException( "Server not available." )
    localFile = open( tempFile, 'wb')
    try:
        downloadSize = int( remoteFile.info().getheaders("Content-Length")[0] )
        downloaded = 0 # Amount downloaded
        blockSize = 8192 # Convenient block size
        while True:
            buffer = remoteFile.read( blockSize )
            if not buffer: # Nothing left to download
                break
            downloaded += len( buffer )
            localFile.write( buffer )
        remoteFile.close()
        localFile.close()
    except (KeyboardInterrupt, SystemExit):
        localFile.close()
        remoteFile.close()
        os.remove( tempFile )
        raise
    if downloaded < downloadSize: # Something has gone wrong
        raise PackageException.PackageException( "Download error", "$i" % downloadSize )
    os.rename( tempFile, os.path.join( kCachePath, fileName ) )
    return "Downloaded %i bytes\n" % downloadSize
    
def ExecuteSimpleCommand( command, args, env, cwd, verbose = False ):
    """ Blocking execute command. Returns True on success"""
    global kCachePath, kInstallPath, kVerbose
    shellCommand = [ command ] + args
    useEnv = os.environ # Default to current environment
    if env is not None:
        for key in env:
            useEnv[key] = env[key]
    process = subprocess.Popen( args = shellCommand, env = useEnv, cwd = cwd, stdout = subprocess.PIPE, stderr = subprocess.PIPE )
    output = ""
    error = ""
    if kVerbose or verbose:
        for line in iter( process.stdout.readline, "" ):
            sys.stdout.write( '\n' + line[:-1] )
            sys.stdout.flush()
            output += '\n' + line[:-1]
        process.wait()
    else:
        output, error = process.communicate()
    output += error
    logText = command + output
    if process.returncode != 0:
        raise PackageException.PackageException( "Command Error", logText )
    return output

def ExecuteComplexCommand( command ):
    """ Execute a multiple line bash command, writes to a temp bash file then executes it."""
    global kCachePath, kInstallPath
    fileName = os.path.join( kInstallPath, "temp.sh" )
    commandFile = open( fileName, "w" )
    commandFile.write( command )
    commandFile.close()
    output = ExecuteSimpleCommand( "/bin/bash", [fileName], os.environ, kInstallPath )
    os.remove( fileName )
    return output

def UnTarFile( tarFileName, targetPath, strip = 0 ):
    """ Untar the file tarFile to targetPath take off the the first strip folders."""
    global kCachePath, kInstallPath
    if strip == 0: # Can untar directly into target
        tarFile = tarfile.open( os.path.join( kCachePath, tarFileName ) )
        tarFile.extractall( targetPath )
        tarFile.close()
    else: # Must untar to temp then to target, note target cannot already exist!
        # First untar to a temp directory
        tempDirectory = os.path.join( kCachePath, "temp" )
        if os.path.exists( tempDirectory ): # Must be an empty temp directory
            shutil.rmtree( tempDirectory )
        tarFile = tarfile.open( os.path.join( kCachePath, tarFileName ) )
        tarFile.extractall( tempDirectory )
        tarFile.close()
        # Now choose how many components to strip
        copyDirectory = tempDirectory
        for iStrip in range( 0, strip ):
            subFolders = os.listdir( copyDirectory )
            if 'pax_global_header' in subFolders:
                subFolders.remove( 'pax_global_header' )
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
    testFile = open( fileName, "w" )
    testFile.write( fileText )
    testFile.close()
    try:
        output = ExecuteSimpleCommand( "g++", [fileName, "-l", libName], os.environ, kInstallPath )
        os.remove( fileName )
        return True, output
    except PackageException.PackageException, e:
        os.remove( fileName )
        return False, e.Pipe

def All(iterable):
    """ New in python 2.5, we target 2.4-tis annoying."""
    for element in iterable:
        if not element:
            return False
    return True
