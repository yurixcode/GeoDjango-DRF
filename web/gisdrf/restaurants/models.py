# Django
from django.contrib.gis.db import models

# Models
from locations.models import Location

# Managers
from .managers import RestaurantManager


class Restaurant(Location):
    """
    Heredamos de Location, el cuál tiene las siguientes propiedades:
        - address = models.CharField(max_length=100, null=True, blank=True)
        - pnt = models.PointField(null=True, blank=True)
        - modified_at = models.DateTimeField(auto_now=True)
        - created_at = models.DateTimeField(auto_now_add=True)
    """

    name = models.CharField(max_length=100)
    twenty_four_hours = models.BooleanField(default=False)

    objects = RestaurantManager()

    def __str__(self):
        return "{} - {}".format(self.name, self.address)

    def getting_location(self):
        pass
