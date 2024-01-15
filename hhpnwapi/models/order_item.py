from django.db import models
from .menu import Menu
from .order import Order

class OrderItem(models.Model):
  order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
  item = models.ForeignKey(Menu, on_delete=models.CASCADE)
  quantity = models.IntegerField()
