#!/usr/bin/env python
#
# Ruby, Gem, XML, XSLT
#
# The gollum (wiki) prerequisites
#
# Author P G Jones - 29/09/2012 <p.g.jones@qmul.ac.uk> : First revision
####################################################################################################
import commandpackage
import librarypackage

class Ruby(commandpackage.CommandPackage):
    """ Checks for ruby."""
    def __init__(self, system):
        super(Ruby, self).__init__("ruby", system, "Install ruby")

class Gem(commandpackage.CommandPackage):
    """ Checks for ruby gems."""
    def __init__(self, system):
        super(Gem, self).__init__("gem", system, "Install ruby-gems")

class XML(librarypackage.LibraryPackage):
    """ Gollum needs xml2-dev."""
    def __init__(self, system):
        super(XML, self).__init__("xml2-dev", system, "Install xml2-dev on this system.", "xml2", 
                                  ["libxml2/libxml/xmlversion.h"])

class XSLT(librarypackage.LibraryPackage):
    """ Gollum needs xslt-dev."""
    def __init__(self, system):
        super(XSLT, self).__init__("xsl-dev", system, "Install xslt2-dev on this system.", "xslt", 
                                   ["libxlst/xlst.h"])
