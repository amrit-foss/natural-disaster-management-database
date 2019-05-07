# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import TornadoDamage, Tornado
from django.contrib import admin

admin.site.register(Tornado)
admin.site.register(TornadoDamage)
