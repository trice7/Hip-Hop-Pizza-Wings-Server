from rest_framework import serializers
from hhpnwapi.models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
  """JSON serializer for employees"""
  
  class Meta:
    model = Employee
    fields = ('id', 'first_name', 'last_name', 'uid', 'is_admin')
