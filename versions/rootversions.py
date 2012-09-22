#!/usr/bin/env python
#
# ROOT5304, ROOT52800, ROOT52400
#
# The root release versions
#
# Author P G Jones - 12/05/2012 <p.g.jones@qmul.ac.uk> : First revision
# Author P G Jones - 13/05/2012 <p.g.jones@qmul.ac.uk> : Added 5.32, 5.28, 5.24 versions (rat v3, v2, v1)
# Author P G Jones - 22/09/2012 <p.g.jones@qmul.ac.uk> : Major refactor of snoing.
####################################################################################################
import root

class ROOT53204(root.Root):
    """ Root 5.32.04, install package."""
    def __init__(self, system):
        """ Initiliase the root 5.32.04 package."""
        super(ROOT53204, self).__init__("root-5.32.04", system, "root_v5.32.04.source.tar.gz")

class ROOT52800(root.Root):
    """ Root 5.28.00, install package."""
    def __init__(self, system):
        """ Initiliase the root 5.32.00 package."""
        super(ROOT52800, self).__init__("root-5.28.00", system, "root_v5.28.00h.source.tar.gz")

class ROOT52400(root.Root):
    """ Root 5.24.00, install package."""
    def __init__(self, system):
        """ Initiliase the root 5.32.00 package."""
        super(ROOT52400, self).__init__("root-5.24.00", system, "root_v5.24.00b.source.tar.gz")
