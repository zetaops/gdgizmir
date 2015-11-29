# -*-  coding: utf-8 -*-
"""project settings"""

# Copyright (C) 2015 ZetaOps Inc.
#
# This file is licensed under the GNU General Public License v3
# (GPLv3).  See LICENSE.txt for details.
__author__ = 'Evren Esat Ozkan'
from zengine.settings import *

import os.path

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

DEBUG = 1

# change this to the actual IP of Riak&Redis servers
SERVER = 'localhost'

RIAK_SERVER = SERVER
REDIS_SERVER = '%s:6379' % SERVER

DEFAULT_LANG = 'tr'

# path of the activity modules which will be invoked by workflow tasks
ACTIVITY_MODULES_IMPORT_PATHS.extend(['gdgizmir.views', ])

# absolute path to the workflow packages
WORKFLOW_PACKAGES_PATHS.append(os.path.join(BASE_DIR, 'diagrams'))

# workflows that does not require logged in user
ANONYMOUS_WORKFLOWS = ['login', ]

# #PYOKO SETTINGS
DEFAULT_BUCKET_TYPE = os.environ.get('DEFAULT_BUCKET_TYPE', 'gdg')

# map your non workflow views here
VIEW_URLS.extend([
    # ('falcon URI template', 'python path to view method/class')
    ('/notify', 'gdgizmir.views.notify'),
])

