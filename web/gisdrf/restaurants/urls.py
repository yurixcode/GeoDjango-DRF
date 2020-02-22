# Django
from django.urls import path

# Views
from .views import HomeView, get_nearby_restaurants


app_name = "restaurants"


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('nearby/<str:x>/<str:y>/', get_nearby_restaurants, name='nearby'),
] 