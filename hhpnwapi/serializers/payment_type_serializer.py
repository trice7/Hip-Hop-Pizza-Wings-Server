from rest_framework import serializers
from hhpnwapi.models import PaymentType

class PaymentTypeSerializer(serializers.ModelSerializer):
  """JSON serializer for payment types"""
  
  class Meta:
    model = PaymentType
    fields = ('id', 'label')
