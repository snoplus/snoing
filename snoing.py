#!/usr/bin/env python
# Author P G Jones - 12/05/2012 <p.g.jones@qmul.ac.uk> : First revision
# SNO+ package manager
import PackageManager
import os
import inspect
import LocalPackage
import SystemPackage

class snoing( PackageManager.PackageManager ):
    """ The package manager for sno+."""
    def __init__( self, cachePath = ".", installPath = "." ):
        super( snoing, self ).__init__()
        # First import all register all packages in this folder
        for module in os.listdir( os.path.dirname( __file__ ) ):
            if module == 'snoing.py' or module[-3:] != '.py':
                continue
            packageSet = __import__( module[:-3], locals(), globals() )
            for name, obj in inspect.getmembers( packageSet ):
                if inspect.isclass( obj ): 
                    if issubclass( obj, LocalPackage.LocalPackage ):
                        self.RegisterPackage( obj( cachePath, installPath ) )
                    elif issubclass( obj, SystemPackage.SystemPackage ):
                        self.RegisterPackage( obj() )

if __name__ == "__main__":
    import optparse
    parser = optparse.OptionParser( usage = "usage: %prog [options] [package]", version="%prog 1.0" )
    (options, args) = parser.parse_args()
    installer = snoing()
    if len(args) == 0:
        #Install all
        print "Installing all"
    else:
        installer.InstallPackage( args[0] )
