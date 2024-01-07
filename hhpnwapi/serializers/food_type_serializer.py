from rest_framework import serializers
from hhpnwapi.models import FoodType

class FoodTypeSerializer(serializers.ModelSerializer):
  """JSON serializer for Food Types"""
  
  class Meta:
    model = FoodType
    fields = ('id', 'label')
