from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField


class Category(models.Model):
    name = models.CharField(max_length=128)
    icon = models.ImageField(upload_to='category')
    about = models.TextField()
    def __str__(self):
        return self.name


class Product(models.Model):
    image = ThumbnailerImageField(blank=True, null=True, resize_source=dict(size=(1600, 1600), sharpen=True), upload_to='products/')
    available = models.PositiveIntegerField(default=0, blank=True)
    title = models.CharField(max_length=20)
    about = models.TextField(max_length=200)
    adding_date = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

class Price(models.Model):
    sum = models.DecimalField(decimal_places=2, max_digits=7)
    product = models.OneToOneField('shop.Product', on_delete=models.CASCADE, related_name='price')

class Sale(models.Model):
    sale = models.OneToOneField('shop.Price', on_delete=models.SET_NULL, null=True)


