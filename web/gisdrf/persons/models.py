# Django
from django.contrib.gis.db import models

class Person(models.Model):
    name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    location = models.PointField(null=True, blank=True)

    def __str__(self):
        return self.name

