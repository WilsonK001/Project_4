from django.db import models


# Create your models here.
class Dog(models.Model):
    name = models.CharField(max_length=32)
    breed = models.CharField(max_length=32)
    age = models.IntegerField()
    gender = models.CharField(max_length=32)
    color = models.CharField(max_length=32)
    image = models.URLField()
    weight = models.IntegerField()