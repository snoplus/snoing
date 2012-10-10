#!/usr/bin/env python
# Author P G Jones - 11/07/2012 <p.g.jones@qmul.ac.uk> : First revision
# Utility module for random useful functions
import os
import pickle
import PackageUtil
import sys
import Log
import Exceptions

def BuildDirectory( path ):
    """ Change the path into a global path and ensure the path exists."""
    globalPath = path
    if path[0] != '/': # Global path
        globalPath = os.path.abspath(os.path.join( os.getcwd(), path ))
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

def CheckSystem():
    """ Check for G4 in the environment and check if mac."""
    # Check the environment is clean
    env = os.environ
    for envbit in env: #check clean environment
        inenv = env[envbit].find('G4')
        if inenv!=-1:
            Log.Error( "G4... environment variables are present, please run in a clean environment." )
            sys.exit(1)
    # Check g++ is installed (python and g++ are the only prerequisites)
    if PackageUtil.FindLibrary( "g++" ) is None:
        Log.Error( "g++ must be installed for snoing to work, try installing build essentials or xcode." )
        sys.exit(1)
    system =  os.uname()[0]
    if system == 'Darwin':
        PackageUtil.kMac = True
        #Check which environments exist
        if "LIBRARY_PATH" not in os.environ:
            os.environ["LIBRARY_PATH"]=""
        if "CPLUS_INCLUDE_PATH" not in os.environ:
            os.environ["CPLUS_INCLUDE_PATH"]=""
        #Append fink or macports directories, if not already appended
        try:
            finkLoc = PackageUtil.ExecuteSimpleCommand("which",["fink"],None,os.getcwd())
        except Exceptions.PackageException:
            finkLoc = ""
        try:
            portLoc = PackageUtil.ExecuteSimpleCommand("which",["port"],None,os.getcwd())
        except Exceptions.PackageException:    
            portLoc = ""
        finkDir = None
        if finkLoc!="" and portLoc!="":
            Log.Warn("Both fink and macports installed, going with fink in dir: %s"%finkLoc)
        if finkLoc!="":
            finkDir = finkLoc.strip().replace("/bin/fink","")
        elif portLoc!="":
            finkDir = portLoc.strip().replace("/bin/port","")
        if finkDir is not None:
            os.environ["PATH"]="%s:%s"%(os.path.join(finkDir,"bin"),os.environ["PATH"])
            os.environ["LIBRARY_PATH"]="%s:%s"%(os.path.join(finkDir,"lib"),os.environ["LIBRARY_PATH"])
            os.environ["CPLUS_INCLUDE_PATH"]="%s:%s"%(os.path.join(finkDir,"include"),os.environ["CPLUS_INCLUDE_PATH"])
        #XCode in 10.7 installs X11 to /usr/X11
        if os.path.exists("/usr/X11"):
            os.environ["PATH"] = "/usr/X11/bin:%s" % os.environ["PATH"]
            os.environ["LIBRARY_PATH"] = "/usr/X11/lib:%s" % os.environ["LIBRARY_PATH"]
            os.environ["CPLUS_INCLUDE_PATH"] = "/usr/X11/include:%s" % os.environ["CPLUS_INCLUDE_PATH"]
        #Frameworks
        if os.path.exists("/System/Library/Frameworks"):
            os.environ["CPLUS_INCLUDE_PATH"] = "/System/Library/Frameworks:%s" % os.environ["CPLUS_INCLUDE_PATH"]
    else:
        PackageUtil.kMac = False
