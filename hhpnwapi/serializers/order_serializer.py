from rest_framework import serializers
from hhpnwapi.models import Order
from .menu_serlializer import MenuSerializer
from .order_item_serlializer import OrderItemSerlializer

class OrderSerializer(serializers.ModelSerializer):
  """JSON serializer for orders"""
  items = OrderItemSerlializer(many=True, read_only=True)
  
  class Meta:
    model = Order
    fields = ('id', 'server', 'is_open', 'subtotal', 'tip', 'tax', 'total', 'customer', 'email', 'phone', 'date', 'type', 'payment', 'items')
    depth = 1
