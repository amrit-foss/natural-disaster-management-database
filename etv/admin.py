# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

admin.site.site_header = 'Disasters Database Admin'

admin.site.register(Earthquake)
admin.site.register(EarthquakeDamage)
admin.site.register(Tsunami)
admin.site.register(TsunamiDamage)
admin.site.register(VolcanicEruption)
admin.site.register(VolcanoDamage)
admin.site.register(QuakeTsunami)
admin.site.register(VolcanoTsunami)