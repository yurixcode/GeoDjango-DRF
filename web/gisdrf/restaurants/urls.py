# Django
from django.urls import path

# Views
from .views import HomeView, get_csv_file


app_name = "restaurants"


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('nearby/@<str:x>/<str:y>/', HomeView.as_view(), name='nearby'),
    path('nearby/csv_file/@<str:x>/<str:y>/', get_csv_file, name='csv_file'),

] 