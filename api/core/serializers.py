from rest_framework import serializers
from .models import Item, Point


class ItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Item
        fields = '__all__'


class PointSerializer(serializers.ModelSerializer):

    class Meta:
        model = Point
        fields = '__all__'