#!/usr/bin/env python
# Author P G Jones - 11/07/2012 <p.g.jones@qmul.ac.uk> : First revision
# Utility module for random useful functions
import os
import pickle

def BuildDirectory( path ):
    """ Change the path into a global path and ensure the path exists."""
    globalPath = path
    if path[0] != '/': # Global path
        globalPath = os.path.join( os.getcwd(), path )
    if not os.path.exists( globalPath ):
        os.makedirs( globalPath )
    return globalPath

def Serialise( path, data ):
    """ Pickle data to path."""
    dataFile = open( path, "w" )
    pickle.dump( data, dataFile )
    dataFile.close()
    return

def DeSerialise( path ):
    """ Unpickle data from path."""
    if os.path.isfile( path ):
        dataFile = open( path, "r" )
        data = pickle.load( dataFile )
        dataFile.close()
        return data
    else:
        return None
