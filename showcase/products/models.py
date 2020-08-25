from django.db import models
from django.contrib.auth.models import User
import uuid
from djmoney.models.fields import MoneyField

class Product(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    name = models.CharField(default='Name', max_length=100, help_text='Product name')
    description = models.CharField(max_length=2000, blank=True, null=True, help_text='Product description')
    price = MoneyField(help_text='Product price', max_digits=14, decimal_places=2, default=0.0, default_currency='RUB')
    unit_price = models.CharField(default='Unit price', max_length=20, help_text='Product unit price')
    active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='images/products', blank=True)
    owner = models.ForeignKey(User, help_text='Product owner', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class Images (models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    order = models.IntegerField(help_text='Field for ordering', null=True)
    image = models.ImageField(upload_to='images/products', blank=True)

    product = models.ForeignKey(Product, default=None, related_name='images', on_delete=models.CASCADE)


