from django.contrib.gis import admin

# Models
from .models import Restaurant

admin.site.register(Restaurant, admin.OSMGeoAdmin)