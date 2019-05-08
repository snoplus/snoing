#!/usr/bin/env python
#
# ROOT5304, ROOT52800, ROOT52400
#
# The root release versions
#
# Author P G Jones - 12/05/2012 <p.g.jones@qmul.ac.uk> : First revision
# Author P G Jones - 13/05/2012 <p.g.jones@qmul.ac.uk> : Added 5.32, 5.28, 5.24 versions (rat v3, v2, v1)
# Author P G Jones - 22/09/2012 <p.g.jones@qmul.ac.uk> : Major refactor of snoing.
#        M Mottram - 20/10/2012 <m.mottram@sussex.ac.uk> : Added 5.34.02
# Author P G Jones - 02/07/2013 <p.g.jones@qmul.ac.uk> : Added 5.34.08
# Author K E gilje - 08/05/2019 <gilje@ualberta.ca> : Added Root 6.16/00
####################################################################################################

import root


class ROOT5Dev(root.RootDevelopment):
    """ROOT 5 Development, install package."""
    def __init__(self, system):
        """Initiliase the ROOT 5 development package."""
        super(ROOT5Dev, self).__init__('root-5-dev', system)


class ROOT61600(root.RootPost60608):
    """Root 6.16.00, install package."""
    def __init__(self, system):
        """Initiliase the root 6.16.00 package."""
        super(ROOT61600, self).__init__('root-6.16.00', system, 'root_v6.16.00.source.tar.gz') 


class ROOT60304(root.Root):
    """Root 6.03.04, install package."""
    def __init__(self, system):
        """Initiliase the root 6.03.08 package."""
        super(ROOT60304, self).__init__('root-6.03.04', system, 'root_v6.03.04.source.tar.gz')


class ROOT53436(root.Root):
    """Root 5.34.36, install package."""
    def __init__(self, system):
        """Initiliase the root 5.34.36 package."""
        super(ROOT53436, self).__init__('root-5.34.36', system, 'root_v5.34.36.source.tar.gz')


class ROOT53434(root.Root):
    """Root 5.34.34, install package."""
    def __init__(self, system):
        """Initiliase the root 5.34.34 package."""
        super(ROOT53434, self).__init__('root-5.34.34', system, 'root_v5.34.34.source.tar.gz')


class ROOT53430(root.Root):
    """Root 5.34.30, install package."""
    def __init__(self, system):
        """Initiliase the root 5.34.30 package."""
        super(ROOT53430, self).__init__('root-5.34.30', system, 'root_v5.34.30.source.tar.gz')


class ROOT53421(root.Root):
    """Root 5.34.21, install package."""
    def __init__(self, system):
        """Initiliase the root 5.34.21 package."""
        super(ROOT53421, self).__init__('root-5.34.21', system, 'root_v5.34.21.source.tar.gz')


class ROOT53418(root.Root):
    """Root 5.34.18, install package."""
    def __init__(self, system):
        """Initiliase the root 5.34.18 package."""
        super(ROOT53418, self).__init__('root-5.34.18', system, 'root_v5.34.18.source.tar.gz')


class ROOT53411(root.Root):
    """Root 5.34.08, install package."""
    def __init__(self, system):
        """Initiliase the root 5.34.02 package."""
        super(ROOT53411, self).__init__('root-5.34.11', system, 'root_v5.34.11.source.tar.gz')


class ROOT53408(root.Root):
    """Root 5.34.08, install package."""
    def __init__(self, system):
        """Initiliase the root 5.34.02 package."""
        super(ROOT53408, self).__init__('root-5.34.08', system, 'root_v5.34.08.source.tar.gz')


class ROOT53402(root.Root):
    """Root 5.34.02, install package."""
    def __init__(self, system):
        """Initiliase the root 5.34.02 package."""
        super(ROOT53402, self).__init__('root-5.34.02', system, 'root_v5.34.02.source.tar.gz')


class ROOT53204(root.Root):
    """Root 5.32.04, install package."""
    def __init__(self, system):
        """Initiliase the root 5.32.04 package."""
        super(ROOT53204, self).__init__('root-5.32.04', system, 'root_v5.32.04.source.tar.gz')


class ROOT52800(root.RootWithConfigure):
    """Root 5.28.00, install package."""
    def __init__(self, system):
        """Initiliase the root 5.32.00 package."""
        super(ROOT52800, self).__init__('root-5.28.00', system, 'root_v5.28.00h.source.tar.gz')


class ROOT52400(root.RootWithConfigure):
    """Root 5.24.00, install package."""
    def __init__(self, system):
        """Initiliase the root 5.32.00 package."""
        super(ROOT52400, self).__init__('root-5.24.00', system, 'root_v5.24.00b.source.tar.gz')
