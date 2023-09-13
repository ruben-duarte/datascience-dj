from django.db import models
from products.models import Product
from customers.models import Customer
from profiles.models import Profile

# Create your models here.
class Position(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.FloatField(blank=True)
    created = models.DateTimeField(blank=True)

    def save(self, *args, **kwargs):
        self.price =self.product.price*self.quantity
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"id: {self.id} , product: {self.product} , quantity: {self.quantity}"


class Sale(models.Model):
    transaction_id = models.CharField(max_length=12, blank=True)
    positions = models.ManyToManyField(Position)
    total_price = models.FloatField(blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    salesman =models.ForeignKey(Profile, on_delete=models.CASCADE)
    created = models.DateTimeField(blank=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"sales for the amount of ${self.total_price}"

class CSV(models.Model):
    pass