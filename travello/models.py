from typing import Any
from django.db import models


# Create your models here.

class Destination(models.Model):
    id = models.AutoField(primary_key=True)
    img = models.ImageField(upload_to='pics', null=True, blank=True)
    name = models.CharField(max_length=100)
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
