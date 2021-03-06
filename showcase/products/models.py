from django.db import models
import uuid
from djmoney.models.fields import MoneyField

class Product(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    name = models.CharField(default='Name', max_length=100, help_text = 'Product name')
    description = models.CharField(max_length=2000, blank=True, null=True, help_text = 'Product description')
    price = MoneyField(help_text='Product price', max_digits=14, decimal_places=2, default=0.0, default_currency='RUB')

    def __str__(self):
        return self.name

class Images (models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    order = models.IntegerField(help_text='Field for ordering', null=True)
    image = models.ImageField(upload_to='images/products', blank=True)

    product = models.ForeignKey(Product, default=None, related_name='images', on_delete=models.CASCADE)


