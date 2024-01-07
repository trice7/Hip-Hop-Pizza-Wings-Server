from rest_framework import serializers
from hhpnwapi.models import Order

class OrderSerializer(serializers.ModelSerializer):
  """JSON serializer for orders"""
  
  class Meta:
    model = Order
    fields = ('id', 'server', 'is_open', 'subtotal', 'tip', 'tax', 'total', 'customer', 'email', 'phone', 'date', 'type', 'payment')
    depth = 1
