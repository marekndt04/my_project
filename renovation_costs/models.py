from django.db import models


# Create your models here.

class Paint(models.Model):
    name = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    production_per_litr = models.DecimalField(max_digits=5, decimal_places=2)
    capacity = models.DecimalField(max_digits=5, decimal_places=2)


class Base(models.Model):
    name = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    production_per_litr = models.DecimalField(max_digits=5, decimal_places=2)
    capacity = models.DecimalField(max_digits=5, decimal_places=2)


class Wallpaper(models.Model):
    name = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    capacity = models.DecimalField(max_digits=5, decimal_places=2)


class WallpaperGlue(models.Model):
    name = models.CharField(max_length=128)
    usage = models.DecimalField(max_digits=5, decimal_places=2)
    capacity = models.DecimalField(max_digits=5, decimal_places=2)
