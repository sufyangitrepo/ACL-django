from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    published_at = models.DateTimeField(auto_now=True)
