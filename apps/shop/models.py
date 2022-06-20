from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=128)
    icon = models.ImageField(upload_to='category')
    about = models.TextField()

class Product(models.Model):
    image = models.ImageField(blank=True, null=True)
    available = models.PositiveIntegerField(default=0, blank=True)
    title = models.CharField(max_length=20)
    about = models.TextField(max_length=200)
    adding_date = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)




