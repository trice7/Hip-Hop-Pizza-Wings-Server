from rest_framework import serializers
from hhpnwapi.models import OrderItem

class OrderItemSerlializer(serializers.ModelSerializer):
  """JSON serializer for an orders items"""
  
  class Meta:
    model = OrderItem
    fields = ('id', 'order', 'item', 'quantity')
    depth = 1
