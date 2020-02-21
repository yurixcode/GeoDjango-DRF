# Django
from django.contrib.gis.db import models

class Location(models.Model):

    address = models.CharField(max_length=100, null=True, blank=True)
    pnt = models.PointField(null=True, blank=True)

    modified_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract=True