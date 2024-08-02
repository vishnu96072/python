from django.contrib.auth import admin
from django.db import models


# Create your models here.
class Wonder(models.Model):
    name=models.CharField(max_length=250)
    desc=models.TextField()
    img=models.ImageField('gallery')
    def __str__(self):
        return self.name
