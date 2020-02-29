# Django
from django.contrib.gis.db import models
from django.conf import settings

# GeoDjango
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance

# Signals
from django.dispatch import receiver
from django.db.models.signals import pre_save

# Models
from locations.models import Location

# Utils
import geocoder


class RestaurantManager(models.Manager):

    def get_restaurants_near_pnt(self, x, y, results=None):
        """
        Aquí vamos a obtener y devolver los restaurantes más 
        cercanos a las cordenadas indicadas...
        """
        queryset =self.annotate(distance=Distance('pnt', self.create_pnt(x, y))
                                                ).exclude(name__exact="no-name"
                                                ).order_by('distance')

        if results:
            return queryset[0:results]

        return queryset
        

    def create_pnt(self, x, y, srid=4326):
        """
        Crearemos el objeto 'Point' con los parámetros recibidos.
        """
        return Point(float(x), float(y), srid=srid)



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



# Signals

@receiver(pre_save, sender=Restaurant)
def getting_location_pnt(sender, instance, **kwargs):
    """
    Obtenemos la dirección introducida, la convertimos a
    cordenadas para después guardarla en la propiedad 'pnt'.
    """
    if not instance.address:
        return

    address = instance.address
    g = geocoder.google(address, key=settings.GOOGLE_API_KEY)
    latitude = g.json.get('lat')
    longitude = g.json.get('lng')
    
    
    pnt = sender.objects.create_pnt(longitude, latitude)

    if instance.pnt != pnt:
        instance.pnt = pnt