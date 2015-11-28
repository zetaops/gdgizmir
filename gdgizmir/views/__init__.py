# -*-  coding: utf-8 -*-
"""
"""

# Copyright (C) 2015 ZetaOps Inc.
#
# This file is licensed under the GNU General Public License v3
# (GPLv3).  See LICENSE.txt for details.
from collections import defaultdict

from pyoko.model import model_registry
from zengine.views import menu
from zengine.dispatch.dispatcher import receiver
from zengine.signals import crud_post_save

from gdgizmir import settings


class Menu(menu.Menu):
    def get_crud_menus(self):
        results = defaultdict(list)
        for mdl in model_registry.get_base_models():
            results['other'].append({"text": mdl.Meta.verbose_name_plural,
                                     "wf": 'crud',
                                     "model": mdl.__name__,
                                     "kategori": settings.DEFAULT_WF_CATEGORY_NAME,
                                     "param": 'id'})
        return results


def notify(current):
    current.output['notifications'] = []


@receiver(crud_post_save)
def set_password(sender, *args, **kwargs):
    if sender.model_class.__name__ == 'User':
        object = kwargs['object']
        password = object.password
        object.set_password(password)
        object.save()
