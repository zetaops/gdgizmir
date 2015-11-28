#!/usr/bin/env python
# -*-  coding: utf-8 -*-
"""
"""

# Copyright (C) 2015 ZetaOps Inc.
#
# This file is licensed under the GNU General Public License v3
# (GPLv3).  See LICENSE.txt for details.
import os.path
import sys
from os import environ

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

# overriding the pip installed zengine with my local clone
sys.path.insert(0, os.path.abspath(os.path.join(BASE_DIR, os.pardir, os.pardir, 'zengine')))

sys.path.insert(0, os.path.abspath(os.path.join(BASE_DIR, os.pardir)))
environ['PYOKO_SETTINGS'] = 'gdgizmir.settings'

from zengine.management_commands import *

if __name__ == '__main__':
    ManagementCommands()
