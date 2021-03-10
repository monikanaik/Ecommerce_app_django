from django.db import models

# Create your models here.


class Product(models.Model):
    name=models.CharField(max_length=40)
    original_price=models.IntegerField()
    discounted_price=models.IntegerField()
    category=models.CharField(max_length=50)
    description=models.TextField()
    image=models.CharField(max_length=200)
