#!/usr/bin/env python
# -*-  coding: utf-8 -*-
"""
"""

# Copyright (C) 2015 ZetaOps Inc.
#
# This file is licensed under the GNU General Public License v3
# (GPLv3).  See LICENSE.txt for details.
from zengine.models import *


class Salon(Model):
    ad = field.String("Salon Adı")

    class Meta:
        verbose_name = 'Salon'
        verbose_name_plural = 'Salonlar'

    def __unicode__(self):
        return "%s" % self.ad


class Konusma(Model):
    konusmaci = field.String("Konuşmacı", index=True)
    tarih = field.Date("Tarihi")
    konu = field.String("Konu", index=True)
    izleyici_sayisi = field.Integer()
    salon = Salon()

    class Meta:
        verbose_name = 'Konuşma'
        verbose_name_plural = 'Konuşmalar'
        list_fields = ['konusmaci', 'konu', 'tarih']

    def __unicode__(self):
        return "%s %s" % (self.konusmaci, self.konu)
