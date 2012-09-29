#!/usr/bin/env python
#
# wiki-rat, wiki-snoing
#
# The documentation wikis
#
# Author P G Jones - 29/09/2012 <p.g.jones@qmul.ac.uk> : First revision
####################################################################################################
import wiki

class RatWiki(wiki.Wiki):
    def __init__(self, system):
        """ Initialise version 1."""
        super(RatWiki, self).__init__("wiki-rat", system, "git@github.com:snoplus/rat.wiki.git")
