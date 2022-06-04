from django.db import models

# Create your models here.
class Coordinates(models.Model):
    lat = models.FloatField(default = 51.477928)
    long = models.FloatField(default = -0.001545)
