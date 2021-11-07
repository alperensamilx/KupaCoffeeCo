from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Categories(models.Model):
    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=32)
    price = models.IntegerField(max_length=8)

    def __str__(self):
        return self.name


class Drinks(models.Model):
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='categories')
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='product')

    def __str__(self):
        return self.categories