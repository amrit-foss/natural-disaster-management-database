# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from django.shortcuts import render


def index(request):
    return render(request, 'etv/home.html')


def quakes(request):
    all_quakes = Earthquake.objects.all
    damage = EarthquakeDamage.objects.all
    context = {'all_quakes': all_quakes, 'damage': damage}
    return render(request, 'etv/quake.html', context)


def tsunami(request):
    all_tsunami = Tsunami.objects.all
    damage = TsunamiDamage.objects.all
    context = {'all_tsunami': all_tsunami, 'damage': damage}
    return render(request, 'etv/tsunami.html', context)


def volcano(request):
    all_eruptions = VolcanicEruption.objects.all
    damage = VolcanoDamage.objects.all
    context = {'all_eruptions': all_eruptions, 'damage': damage}

    return render(request, 'etv/volcano.html', context)
