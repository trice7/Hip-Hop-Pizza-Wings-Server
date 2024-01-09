"""View module for handling requests for orders"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from hhpnwapi.models import Order, Employee, OrderType, PaymentType
from hhpnwapi.serializers import OrderSerializer

class OrderView(ViewSet):
  """Hip Hop, Pizza, & Wings Order View"""
  
  def retrieve(self, request, pk):
    """Handle GET request for a single order
    
    Returns -> Response -- JSON serialized order"""
    
    try:
      order = Order.objects.get(pk=pk)
      serializer = OrderSerializer(order)
      return Response(serializer.data)
    except Order.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
  def list(self, reqeust):
    """Handle GET requests for all orders
    
    Returns -> Response -- JSON serialized list of orders"""
    
    try:
      orders = Order.objects.all()
      serializer = OrderSerializer(orders, many=True)
      return Response(serializer.data)
    except Order.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
  def create(self, request):
    """Handle POST request for orders
    Returns -> JSON serialized order instance with 201 status"""
    server = Employee.objects.get(pk=request.data['server'])
    type = OrderType.objects.get(pk=request.data['type'])
    payment = PaymentType.objects.get(pk=request.data['payment'])
    
    order = Order.objects.create(
      server = server,
      is_open = request.data['isOpen'],
      subtotal = request.data['subtotal'],
      tip = request.data['tip'],
      tax = request.data['tax'],
      total = request.data['total'],
      customer = request.data['customer'],
      email = request.data['email'],
      phone = request.data['phone'],
      type = type,
      payment = payment,
    )
    
    serializer = OrderSerializer(order)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  
  def update(self, request, pk):
    """Handles PUT requests for an order
    
    Returns -> JSON serialized order instance with 200 status"""
    
    server = Employee.objects.get(pk=request.data['server'])
    type = OrderType.objects.get(pk=request.data['type'])
    payment = PaymentType.objects.get(pk=request.data['payment'])
    
    order = Order.objects.get(pk=pk)
    
    order.server = server
    order.is_open = request.data['isOpen']
    order.subtotal = request.data['subtotal']
    order.tip = request.data['tip']
    order.tax = request.data['tax']
    order.total = request.data['total']
    order.customer = request.data['customer']
    order.email =request.data['email']
    order.phone = request.data['phone']
    order.type = type
    order.payment = payment
    
    order.save()
    serializer = OrderSerializer(order)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  def destroy(self, reqeust, pk):
    """Handles Delete request for an order
    
    Returns -> Empty body with 204 status"""
    
    order = Order.objects.get(pk=pk)
    order.delete()
    return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    