from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField()
    category = models.CharField(max_length=50)

    def clean(self):
        if self.price <= 0:
            raise ValidationError("Price must be greater than or equal to 0")
    
    def __str__(self):
        return self.name