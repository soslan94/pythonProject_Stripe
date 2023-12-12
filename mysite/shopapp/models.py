from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(max_length=3000, blank=True)
    price = models.IntegerField(default=0)