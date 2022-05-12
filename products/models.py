from django.db import models
from categories.models import Category


class Product(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.title
