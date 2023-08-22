from django.db import models

# Create your models here.


class registration(models.Model):
    username = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    password = models.CharField(max_length=500)

class tabledata(models.Model):
    length = models.CharField(max_length=500)
    width = models.CharField(max_length=500)
    height = models.CharField(max_length=500)
    area = models.CharField(max_length=500)
    volume = models.CharField(max_length=500)