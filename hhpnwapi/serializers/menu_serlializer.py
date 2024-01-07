from rest_framework import serializers
from hhpnwapi.models import Menu

class MenuSerializer(serializers.ModelSerializer):
  """JSON serializer for the menu"""
  
  class Meta:
    model = Menu
    fields = ('id', 'name', 'cost', 'description', 'type')
    depth = 1
