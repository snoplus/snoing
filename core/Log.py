#!/usr/bin/env python
# Author P G Jones - 14/06/2012 <p.g.jones@qmul.ac.uk> : First revision
#        P G Jones - 21/06/2012 <p.g.jones@qmul.ac.uk> : Second revision, file usage
# Logs text to the screen
import sys

class LogFile( object ):
    """ Opens and manages a log file."""
    def __init__( self, filePath = None, append = False ):
        """ Open the correct file."""
        if filePath is None:
            self._File = None
            return
        if not append and os.path.exists( filePath ):
            os.remove( filePath )
        self._File = open( filePath, "a" )
        return
    def Write( self, text ):
        """ Write the text to the file."""
        if self._File is not None:
            self._File.write( "%s\n" % text )
        return
    def __del__( self ):
        """ Closes the file."""
        if self._File is not None:
            self._File.close()

kDetialsFile = LogFile() # Empty default file
kLogFile = LogFile()     # Empty default file

kHeader = '\033[95m'
kOKBlue = '\033[94m'
kOKGreen = '\033[92m'
kWarning = '\033[93m'
kFail = '\033[91m'
kEnd = '\033[0m'

def Header( text ):
    """ Output summery of what is to happen next."""
    kDetailsFile.Write( "## %s" % text )
    print kHeader + text + kEnd

def Info( text ):
    """ Output short and useful infomation to the screen."""
    kDetailsFile.Write( text )
    print kOKBlue + text + kEnd

def Result( text ):
    """ Output a result (usually success or it will warn)."""
    kLogFile.Write( text )
    kDetailsFile.Write( text )
    print kOKGreen + text + kEnd

def Detail( text ):
    """ Output long information to the screen."""
    kDetailsFile.Write( text )
    print text

def Warn( text ):
    """ Output a warning to the screen."""
    kDetailsFile.Write( text )
    print kWarning + text + kEnd

def Error( text ):
    """ Ouput a error to the screen."""
    kDetailsFile.Write( text )
    print kFail + text + kEnd
