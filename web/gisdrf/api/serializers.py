# Django DRF
from rest_framework import serializers

# Models
from restaurants.models import Restaurant

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'address', 'location')
        read_only_fields = ('location',)