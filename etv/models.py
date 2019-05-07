from __future__ import unicode_literals
from django.db import models


class Earthquake(models.Model):
    earthquake_id = models.PositiveIntegerField(primary_key='true')
    intensity = models.DecimalField(max_digits=5, max_length=5, decimal_places=2)
    date = models.DateField()
    country = models.CharField(max_length=255, default=None)
    place = models.CharField(max_length=255, default=None)
    latitude = models.DecimalField(max_digits=5, max_length=5, decimal_places=2)
    longitude = models.DecimalField(max_digits=5, max_length=5, decimal_places=2)

    def __str__(self):
        return str(self.earthquake_id)+' '+self.country+' '+self.place


class Tsunami(models.Model):
    tsunami_id = models.PositiveIntegerField(primary_key='true')
    date = models.DateField()
    country = models.CharField(max_length=256, default=None)
    place = models.CharField(max_length=256, default=None)
    wave_height = models.DecimalField(max_digits=5, max_length=5, decimal_places=2)
    spread_area = models.DecimalField(max_digits=5, max_length=5, decimal_places=2)

    def __str__(self):
        return str(self.tsunami_id)+' '+self.country+' '+self.place


class VolcanicEruption(models.Model):
    TYPES = (
        ('magma', 'Magmatic eruption'),
        ('phreato', 'Phreatomagmatic eruption')
    )
    SUB_TYPES = (
        ('m-Hawaiian', 'Magmatic Hawaiian'),
        ('m-Strombolian', 'Magmatic Strombolian'),
        ('m-Vulcanian', 'Magmatic Vulcanian'),
        ('m-Pelean', 'Magmatic Pelean'),
        ('p-Surtseyan', 'Phreatomagmatic Surtseyan'),
        ('p-Submarine', 'Phreatomagmatic Submarine'),
        ('p-Subglacial', 'Phreatomagmatic Subglacial')
    )
    volcano_id = models.PositiveIntegerField(primary_key='true')
    mountain = models.CharField(max_length=256)
    location = models.CharField(max_length=256)
    year = models.PositiveIntegerField()
    type = models.CharField(max_length=256, choices=TYPES)
    subtype = models.CharField(max_length=256, choices=SUB_TYPES)
    spread_area = models.PositiveIntegerField()

    def __str__(self):
        return str(self.volcano_id)+' '+self.location


class EarthquakeDamage(models.Model):
    earthquake_id = models.OneToOneField(Earthquake, primary_key='true', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=5, max_length=5, decimal_places=2)
    deaths = models.PositiveIntegerField()
    house_destroyed = models.PositiveIntegerField()
    bridges_destroyed = models.PositiveIntegerField(default=2)

    def __str__(self):
        return str(self.earthquake_id)+' '+str(self.amount)+' '+'million of damage'


class TsunamiDamage(models.Model):
    tsunami_id = models.OneToOneField(Tsunami, primary_key='true', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=5, max_length=5, decimal_places=2)
    deaths = models.PositiveIntegerField()
    house_destroyed = models.PositiveIntegerField()
    bridge_destroyed = models.PositiveIntegerField(default=2)

    def __str__(self):
        return str(self.tsunami_id)+' '+str(self.amount)+' '+'million of damage'


class VolcanoDamage(models.Model):
    volcano_id = models.OneToOneField(VolcanicEruption, primary_key='true', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=5, max_length=5, decimal_places=2)
    deaths = models.PositiveIntegerField()
    house_destroyed = models.PositiveIntegerField()

    def __str__(self):
        return str(self.volcano_id)+' '+str(self.amount)+' '+'million of damage'


class QuakeTsunami(models.Model):
    tsunami_id = models.OneToOneField(Tsunami, on_delete=models.CASCADE)
    earthquake_id = models.ForeignKey(Earthquake, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.earthquake_id)+' '+str(self.tsunami_id)


class VolcanoTsunami(models.Model):
    tsunami_id = models.ForeignKey(Tsunami, on_delete=models.CASCADE)
    volcano_id = models.ForeignKey(VolcanicEruption, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.volcano_id)+' '+str(self.tsunami_id)
