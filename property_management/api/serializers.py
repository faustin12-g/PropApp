from rest_framework import serializers
from property_app.models import *

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ['id', 'name', 'address', 'property_type', 'number_of_units']


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ['id', 'bedrooms', 'bathrooms', 'rent', 'is_available']

