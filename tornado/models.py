from __future__ import unicode_literals
from django.db import models


class Tornado(models.Model):
    FUJITA_SCALE = (
        ('F0', 'Light damage'),
        ('F1', 'Moderate damage'),
        ('F2', 'Considerable damage'),
        ('F3', 'Severe damage'),
        ('F4', 'Devastating damage'),
        ('F5', 'Incredible damage')
    )
    ROTATION = (
        ('Clock', 'ClockWise'),
        ('A-Clock', 'Anti Clockwise')
    )
    tornado_id = models.PositiveIntegerField()
    rotation = models.CharField(max_length=25, choices=ROTATION)
    date = models.DateField()
    wind_speed = models.DecimalField(max_length=5, max_digits=5, decimal_places=2)
    start_location = models.CharField(max_length=255)
    end_location = models.CharField(max_length=255)
    distance_covered = models.CharField(max_length=25)
    fujita_scale_rating = models.CharField(max_length=256, choices=FUJITA_SCALE)

    def __str__(self):
        return str(self.tornado_id) + ' ' + self.start_location


class TornadoDamage(models.Model):
    tornado_id = models.ForeignKey(Tornado,on_delete=models.CASCADE)
    amount = models.DecimalField(max_length=5, max_digits=5, decimal_places=2)
    deaths = models.PositiveIntegerField()
    bridges = models.PositiveIntegerField(default=0)
    house_destroyed = models.PositiveIntegerField()

    def __str__(self):
        return str(self.tornado_id) + ' ' + str(self.amount)+' millions loss'
