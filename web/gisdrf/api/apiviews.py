# Django
from django.shortcuts import render
from django.conf import settings

# GeoDjango
from django.contrib.gis.geos import GEOSGeometry, Point

# Django Rest Framework
from rest_framework import generics

# APIViews
from rest_framework import viewsets

# Models
from restaurants.models import Restaurant
from persons.models import Person

# Serializers
from .serializers import RestaurantSerializer, PersonSerializer

# Utils
import geocoder



class RestaurantListView(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class PersonListView(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def perform_create(self, serializer):
        """
        Validamos y guardamos el formato de las cordenadas introducida.
        """
        pnt_location = serializer.initial_data['pnt']

        # Separamos los valores introducidos por el usuario
        location = pnt_location.split(' ')
        pnt = Point(float(location[0]), float(location[1]))

        serializer.save(pnt=pnt)
