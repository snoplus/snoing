#!/usr/bin/env python
# Author P G Jones - 14/06/2012 <p.g.jones@qmul.ac.uk> : First revision
# Logs text to the screen
import sys

kHeader = '\033[95m'
kOKBlue = '\033[94m'
kOKGreen = '\033[92m'
kWarning = '\033[93m'
kFail = '\033[91m'
kEnd = '\033[0m'

def Info( text ):
    """ Output short and useful infomation to the screen."""
    print kHeader + text + kEnd

def Result( text ):
    """ Output a result (usually success or it will warn)."""
    print kOKBlue + text + kEnd

def Detail( text ):
    """ Output long information to the screen."""
    print text

def Warn( text ):
    """ Output a warning to the screen."""
    print kWarning + text + kEnd

def Error( text ):
    """ Ouput a error to the screen."""
    print kFail + text + kEnd
