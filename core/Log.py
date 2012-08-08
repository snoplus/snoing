#!/usr/bin/env python
# Author P G Jones - 14/06/2012 <p.g.jones@qmul.ac.uk> : First revision
#        P G Jones - 21/06/2012 <p.g.jones@qmul.ac.uk> : Second revision, file usage
# Logs text to the screen
import sys
import os
import PackageUtil

class LogFile( object ):
    """ Opens and manages a log file."""
    def __init__( self, filePath = None, append = False ):
        """ Open the correct file."""
        self._FilePath = filePath
        if filePath is not None and not append and os.path.exists( filePath ):
            os.remove( filePath )
            file = open( self._FilePath, "w" )
            file.write( "## SNOING\nThis is a snoing install directory. Please alter only with snoing at %s" % __file__ )
            file.close()
        return
    def Write( self, text ):
        """ Write the text to the file."""
        if self._FilePath is None:
            return
        file = open( self._FilePath, "a" )
        file.write( "%s\n" % text )
        file.close()
        return

kDetailsFile = LogFile() # Empty default file
kLogFile = LogFile()     # Empty default file

kHeader = '\033[95m'
kOKBlue = '\033[94m'
kOKGreen = '\033[92m'
kWarning = '\033[93m'
kFail = '\033[91m'
kEnd = '\033[0m'

def Header( text ):
    """ Output summery of what is to happen next."""
    kDetailsFile.Write( text )
    print kHeader + text + kEnd

def Info( text ):
    """ Output short and useful infomation to the screen."""
    kDetailsFile.Write( text )
    print kOKBlue + text + kEnd

def Result( text ):
    """ Output a result (usually success or it will warn)."""
    kDetailsFile.Write( text )
    print kOKGreen + text + kEnd

def Detail( text ):
    """ Output long information to the screen."""
    kDetailsFile.Write( text )
    if PackageUtil.kVerbose:
        print text

def Warn( text ):
    """ Output a warning to the screen."""
    kDetailsFile.Write( text )
    print kWarning + text + kEnd

def Error( text ):
    """ Ouput a error to the screen."""
    kDetailsFile.Write( text )
    print kFail + text + kEnd
