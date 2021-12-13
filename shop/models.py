from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Product name")
    description = models.TextField(max_length=1000, verbose_name="Description")
