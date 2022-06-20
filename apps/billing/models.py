from django.db import models
from apps.shop.models import Product

class Order(models.Model):
    product_list = models.ManyToManyField(Product, symmetrical=False)


class Payment(models.Model):
    STATUS_LIST = [
        ('pending', 'Pending'),
        ('success', 'Success'),
        ('error', 'Error'),
        ('cancel', 'Cancel'),
    ]
    client = models.EmailField()
    payment_system = models.CharField(max_length=64)
    status = models.CharField(max_length=32, choices=STATUS_LIST)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    sum = models.PositiveIntegerField()
    time_pay = models.DateTimeField(blank=True, null=True)
    time_add = models.DateTimeField(auto_now=True)