# -*-  coding: utf-8 -*-
"""
"""

# Copyright (C) 2015 ZetaOps Inc.
#
# This file is licensed under the GNU General Public License v3
# (GPLv3).  See LICENSE.txt for details.

from zengine.dispatch.dispatcher import receiver
from zengine.signals import crud_post_save


# faking notify to satisfy frontend
def notify(current):
    current.output['notifications'] = []

# encrypting password on save
@receiver(crud_post_save)
def set_password(sender, *args, **kwargs):
    if sender.model_class.__name__ == 'User':
        object = kwargs['object']
        password = object.password
        if password.startswith('$pbkdf2'):
            return # already encrypted, password unchanged
        object.set_password(password)
        object.save()
