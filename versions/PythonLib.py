#!/usr/bin/env python
# Author P G Jones - 11/07/2012 <p.g.jones@qmul.ac.uk> : First revision
# The python libraries are special
import CommandPackage
import SystemPackage
import PackageUtil

class Python( CommandPackage.CommandPackage ):
    """ Package for the python development library."""
    def __init__( self ):
        super( Python, self ).__init__( "python", "Install python on this system, how on earth is this possible? snoing is written in python")
        return

class PythonDev( SystemPackage.SystemPackage ):
    """ Package for the python development library."""
    def __init__( self ):
        super( PythonDev, self ).__init__( "python-dev", "Install python dev on this system." )
        return
    def CheckState( self ):
        """ Check the python-dev install state."""
        # First check for python config
        if PackageUtil.FindLibrary( "python-config" ) is not None:
            # Now can test for linking
            print 'check config'
            installed, self._CheckPipe = PackageUtil.TestConfigLibrary( "python-config", "Python.h")
            print 'python:',installed
            self._Installed = installed
        elif PackageUtil.FindLibrary( "rpm" ) is not None:
            print 'check rpm'
            installed = PackageUtil.TestConfigRPM( "python-devel" )
            print 'python:',installed
            self._Installed = installed
        return
