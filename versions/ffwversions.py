#!/usr/bin/env python
#
# FFTWVersions
#
# FFTW releases
#
# Author:
#  - 2015-06-05 M Mottram <m.mottram@qmul.ac.uk> first instance
#
####################################################################################################
import fftw

class Fftw334(fftw.Fftw):
    """ Package for fftw. """
    def __init__(self, system):
        """ Initialize the package, set the name."""
        super(Fftw334, self).__init__("fftw-3.3.4", system, "fftw-3.3.4.tar.gz")


    
