from django.db import models

# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=200)
    # headline = models.CharField(max_length=200)
    # sub_headline = models.CharField(max_length=200, null=True, blank=True)
    # thumbnail = models.ImageField(null=True, blank=True, upload_to="images", default="placeholder.png")
    # body = RichTextUploadingField(null=True, blank=True)
    # created = models.DateTimeField(auto_now_add=True)
    # active = models.BooleanField(default=False)
    # featured = models.BooleanField(default=False)
    # tags = models.ManyToManyField(Tag, null=True, blank=True)
    # slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    # price =
    # img =
    # featured =
    # active =

    def __str__(self):
        return self.name

