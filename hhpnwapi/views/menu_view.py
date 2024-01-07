"""View module for handling request for menu"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from hhpnwapi.models import Menu
from hhpnwapi.serializers import MenuSerializer

class MenuView(ViewSet):
  """Hip Hop, Pizza, & Wings Menu View"""
  
  def retrieve(self, request, pk):
    """Handle GET request for a single menu item
    
    Returns -> Response -- JSON serlialized menu"""
    
    try:
      menu = Menu.objects.get(pk=pk)
      serializer = MenuSerializer(menu)
      return Response(serializer.data)
    except Menu.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
  def list(self, request):
    """Handles GET request for all menu items
    
    Returns -> Response -- JSON serialized list of artists"""
    
    try:
      menus = Menu.objects.all()
      serializer = MenuSerializer(menus, many=True)
      return Response(serializer.data)
    except Menu.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
  #
