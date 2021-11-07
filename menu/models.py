from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Categories(models.Model):
    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name


class Drinks(models.Model):
    name = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='drinks')
    price = models.IntegerField(max_length=8)

    def __str__(self):
        return self.name