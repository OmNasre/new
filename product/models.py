from django.db import models
from django.utils import timezone

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    
    def __str__(self):
        return self.name
    
    
class Contact(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    user_name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_name} - {self.product.name}"