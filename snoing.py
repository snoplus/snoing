#!/usr/bin/env python
# Author P G Jones - 12/05/2012 <p.g.jones@qmul.ac.uk> : First revision
# SNO+ package manager
import PackageManager
import os

class snoing( PackageManager.PackageManager ):
    """ The package manager for sno+."""
    def __init__( self, cachePath = ".", installPath = "." ):
        super( snoing, self ).__init__()
        # First import all register all packages in this folder
        for module in os.listdir( os.path.dirname( __file__ ) ):
            if module == 'snoing.py' or module[-3:] != '.py':
                continue
            packageSet = __import__( module[:-3], locals(), globals() )
            for key, package in packageSet.PackageDict.items():
                self.RegisterPackage( package( cachePath, installPath ) )
        # Now choose

                
installer = snoing()
installer.InstallPackage( "root-5.32.03" )
