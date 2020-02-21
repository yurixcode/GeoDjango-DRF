# Django DRF
from rest_framework import serializers

# Models
from restaurants.models import Restaurant
from persons.models import Person


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'address', 'pnt', 'twenty_four_hours')
        read_only_fields = ('pnt',)


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        # fields = ('id', 'first_name', 'last_name', 'location', 'address')
        fields = '__all__'
        read_only_fields = ('address',)