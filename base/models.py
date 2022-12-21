from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    #image =
    tag = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    #price =
    #previous_price =
    #availability =
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    #image1 =
    created = models.DateTimeField(auto_now_add=True)
    timeTaken = models.CharField(max_length=50)
    data = models.TextField(null=False, blank=False)