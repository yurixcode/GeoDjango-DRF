# Django
from django.views import generic
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

# GeoDjango
from django.contrib.gis.geos import fromstr, Point
from django.contrib.gis.db.models.functions import Distance

# Models
from .models import Restaurant

longitude = -1.1410261
latitude = 38.0030997
# user_location = Point(longitude, latitude, srid=4326)

class HomeView(View):
    template_name = "restaurants/index.html"

    def get(self, request, *args, **kwargs):
        """
        GET
        """
        
        return render(request, self.template_name)


def user_location(x, y):
    """
    Obtenemos la localización del usuario
    """
    return Point(float(x), float(y), srid=4326)

def get_queryset(x, y):
    queryset = Restaurant.objects.annotate(distance=Distance('pnt', user_location(x, y))
                                        ).exclude(name__exact="no-name"
                                        ).order_by('distance')[0:10]
    
    return queryset


def get_nearby_restaurants(request, x, y):
    template_name = 'restaurants/index.html'

    if request.method == "GET":
        queryset = get_queryset(x, y)

        context = {'restaurants': queryset}    
        
        return render(request, template_name, context)
