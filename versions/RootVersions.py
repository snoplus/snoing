#!/usr/bin/env python
# Author P G Jones - 12/05/2012 <p.g.jones@qmul.ac.uk> : First revision
# Author P G Jones - 13/05/2012 <p.g.jones@qmul.ac.uk> : Added 5.32, 5.28, 5.24 versions (rat v3, v2, v1)
# The ROOT packages (versions)
import Root

class ROOT53204( Root.Root ):
    """ Root 5.32.04, install package."""
    def __init__( self ):
        """ Initiliase the root 5.32.04 package."""
        super( ROOT53203, self ).__init__( "root-5.32.04", "root_v5.32.04.source.tar.gz" )
        return

class ROOT52800( Root.Root ):
    """ Root 5.28.00, install package."""
    def __init__( self ):
        """ Initiliase the root 5.32.00 package."""
        super( ROOT52800, self ).__init__( "root-5.28.00", "root_v5.28.00h.source.tar.gz" )
        return

class ROOT52400( Root.Root ):
    """ Root 5.24.00, install package."""
    def __init__( self ):
        """ Initiliase the root 5.32.00 package."""
        super( ROOT52400, self ).__init__( "root-5.24.00", "root_v5.24.00b.source.tar.gz" )
        return

