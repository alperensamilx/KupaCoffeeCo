from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Categories(models.Model):
    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=32)
    price = models.IntegerField()

    def __str__(self):
        return self.name

