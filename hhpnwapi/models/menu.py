from django.db import models
from .food_type import FoodType

class Menu(models.Model):
  name = models.CharField(max_length=50)
  cost = models.DecimalField(max_digits=7, decimal_places=2)
  description = models.TextField()
  type = models.ForeignKey(FoodType, on_delete=models.CASCADE)
