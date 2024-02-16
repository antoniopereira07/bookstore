from django.db import models
from product.models.category import Category


class Product(models.Model):
    title: models.CharField = models.CharField(max_length=100)
    description: models.TextField = models.TextField(
        max_length=500, blank=True, null=True
    )
    price: models.PositiveIntegerField = models.PositiveIntegerField(null=True)
    active: models.BooleanField = models.BooleanField(default=True)
    category: models.ManyToManyField = models.ManyToManyField(
        Category, blank=True
    )
