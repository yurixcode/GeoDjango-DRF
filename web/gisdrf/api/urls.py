# Django
from django.urls import path, include

# Routers
from rest_framework.routers import DefaultRouter

# API Viewsets
from .apiviews import RestaurantListView


app_name = "api"

# router = DefaultRouter()
# router.register('v1/restaurants', RestaurantListView, basename='restaurants')


urlpatterns = [
    path('v1/restaurants/', RestaurantListView.as_view(), name='restaurants_list'),
] 

# urlpatterns += router.urls