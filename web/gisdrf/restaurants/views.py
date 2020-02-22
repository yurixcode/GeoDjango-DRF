# Django
from django.shortcuts import render
from django.views import View

# GeoDjango
from django.contrib.gis.geos import fromstr, Point
from django.contrib.gis.db.models.functions import Distance

# Models
from .models import Restaurant


class HomeView(View):
    template_name = "restaurants/index.html"

    def get(self, request, x=None, y=None, *args, **kwargs):
        """
        GET
        """
        context = {}

        if x and y:
            """
            Obtenemos los restaurantes más cercanos al usuario,
            a partir de las cordenadas obtenidas...
            """
            nearby_restaurants = Restaurant.objects.get_restaurants_near_pnt(x, y)
            context['restaurants'] = nearby_restaurants
        
        return render(request, self.template_name, context)
