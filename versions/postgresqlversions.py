#!/usr/bin/env python
#
# The PostgreSQL release versions
#
# Author M Mottram - 06/06/2016 <m.mottram@qmul.ac.uk> : First revision
####################################################################################################
import postgresql

class PostgreSQL952(postgresql.PostgreSQL):
    """ PostgreSQL 9.5.2, install package"""

    def __init__(self, system):
        """Initialise the PostgreSQL 9.5.2 package."""
        super(PostgreSQL952, self).__init__("postgresql-9.5.2", system, "9.5.2")
