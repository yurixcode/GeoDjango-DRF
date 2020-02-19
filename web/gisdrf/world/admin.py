from django.contrib.gis import admin

# Models
from .models import WorldBorder

admin.site.register(WorldBorder, admin.OSMGeoAdmin)