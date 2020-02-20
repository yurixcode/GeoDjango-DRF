# Django
from django.shortcuts import render

# Django DRF
from rest_framework import generics

# APIViews
from rest_framework import viewsets

# Models
from restaurants.models import Restaurant

# Serializers
from .serializers import RestaurantSerializer

# Utils
import geocoder


class RestaurantListView(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    # def perform_create(self, serializer):
    #     address = serializer.initial_data['address']
    #     g = geocoder.google(address)
    #     latitude = g.latlng[0]
    #     longitude = g.latlng[1]
    #     pnt = "POINT(" + str(longitude) + ' ' + str(latitude) + ")"
    #     serializer.save(location=pnt)

