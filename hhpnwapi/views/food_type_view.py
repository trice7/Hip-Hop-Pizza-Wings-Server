"""View module for handling requests for food types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from hhpnwapi.models import FoodType
from hhpnwapi.serializers import FoodTypeSerializer

class FoodTypeView(ViewSet):
  """Hip Hop, Pizza, & Wings Food Type View"""
  
  def retrieve(self, request, pk):
    """Handle GET requests for a single food type
    
    Returns -> Response -- JSON serialized foodtype"""
    
    try:
      foodtype = FoodType.objects.get(pk=pk)
      serializer = FoodTypeSerializer(foodtype)
      return Response(serializer.data)
    except FoodType.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
  def list(self, request):
    """Handle GET requests for all orders
    
    Returns -> Response -- JSON serialized list of food types"""
    
    try:
      foodtypes = FoodType.objects.all()
      serializer = FoodTypeSerializer(foodtypes, many=True)
      return Response(serializer.data)
    except FoodType.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
  #
