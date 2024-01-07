from django.db import models
from .user import Employee
from .order_type import OrderType
from .payment_type import PaymentType

class Order(models.Model):
  server = models.ForeignKey(Employee, on_delete=models.CASCADE)
  is_open = models.BooleanField()
  subtotal = models.DecimalField(max_digits=7, decimal_places=2)
  tip = models.DecimalField(max_digits=7, decimal_places=2)
  tax = models.DecimalField(max_digits=7, decimal_places=2)
  total = models.DecimalField(max_digits=7, decimal_places=2)
  customer = models.CharField(max_length=50)
  email = models.CharField(max_length=50)
  phone = models.CharField(max_length=20)
  date=models.DateField(auto_now_add=True)
  type = models.ForeignKey(OrderType, on_delete=models.CASCADE)
  payment = models.ForeignKey(PaymentType, on_delete=models.CASCADE)
