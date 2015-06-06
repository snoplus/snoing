#!/usr/bin/env python
#
# GSLVersions
#
# GSL releases: ROOT seems to require GSL 1.1
#
# Author:
#  - 2015-06-05 M Mottram <m.mottram@qmul.ac.uk> first instance
#
####################################################################################################
import gsl

class Gsl116(gsl.Gsl):
    """ Package for gsl. """
    def __init__(self, system):
        """ Initialize the package, set the name."""
        super(Gsl116, self).__init__("gsl-1.16", system, "gsl-1.16.tar.gz")


    
