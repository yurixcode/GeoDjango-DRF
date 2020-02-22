# Django
from django.urls import path

# Views
from .views import HomeView


app_name = "restaurants"


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('nearby/@<str:x>-<str:y>/', HomeView.as_view(), name='nearby'),
] 