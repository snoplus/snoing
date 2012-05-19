#!/usr/bin/env python
# Author P G Jones - 19/05/2012 <p.g.jones@qmul.ac.uk> : First revision
# Takes care of packages that are system installed libraries e.g. X11
import Package
import PackageUtil

class CommandPackage( Package.Package ):
    """ For packages that are simple commands such as make."""
    def __init__( self, name, libName, header = None ):
        """ Initialise the package."""
        super( CommandPackage, self ).__init__( name )
        self._Mode = 0 # 0 is initial, 1 is installed
        self._LibName = libName
        self._Header = header
        return
    def IsInstalled( self ):
        """ Check and return if package is installed."""
        return self._Mode > 0
    def CheckState( self ):
        """ Derived classes should override this to ascertain the package status, downloaded? installed?"""
        if PackageUtil.TestLibrary( self._LibName, self._Header ) == False:
            print "%s is not installed." % self._Name
        else:
            self._Mode = 1
        return
