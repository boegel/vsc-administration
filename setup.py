#!/usr/bin/env python
# -*- coding: latin-1 -*-
##
# Copyright 2012-2013 Ghent University
#
# This file is part of vsc-administration,
# originally created by the HPC team of Ghent University (http://ugent.be/hpc/en),
# with support of Ghent University (http://ugent.be/hpc),
# the Flemish Supercomputer Centre (VSC) (https://www.vscentrum.be),
# the Flemish Research Foundation (FWO) (http://www.fwo.be/en)
# and the Department of Economy, Science and Innovation (EWI) (http://www.ewi-vlaanderen.be/en).
#
# All rights reserved.
#
##
"""
vsc-administration distribution setup.py

@author: Andy Georges (Ghent University)
@author: Jens Timmerman (Ghent University)
"""

from vsc.install import shared_setup
from vsc.install.shared_setup import ag, jt

PACKAGE = {
    'version': '1.5.2',
    'author': [ag, jt],
    'maintainer': [ag, jt],
    'tests_require': ['mock'],
    'makesetupcfg': False,  # use setup.cfg provided to get pytz instead of python-pytz
    'install_requires': [
        'vsc-accountpage-clients >= 0.9.1',
        'vsc-base >= 2.8.3',
        'vsc-config >= 1.35.3',
        'vsc-filesystems >= 0.19',
        'vsc-ldap >= 1.1',
        'pytz',
        'python-ldap',
        'vsc-ldap-extension >= 1.3',
        'vsc-utils >= 1.9.1',
        'lockfile >= 0.9.1',
        'enum34',
    ],
}


if __name__ == '__main__':
    shared_setup.action_target(PACKAGE)
