from django.db import models
from django.contrib.auth.models import User
import uuid
from djmoney.models.fields import MoneyField
from PIL import Image


def upload_product_image_to(instance, filename):
    return 'images/products/%s/%s' % (instance.owner.id, filename)


def upload_showcase_image_to(instance, filename):
    return 'images/showcase/%s/%s' % (instance.owner.id, filename)


class Showcase(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    title = models.CharField(max_length=100, help_text='Showcase title')
    image = models.ImageField(upload_to=upload_showcase_image_to, blank=True)
    owner = models.ForeignKey(User, help_text='Owner', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title


class ShowcaseInfo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    title = models.CharField(max_length=100, help_text='Info block title')
    description = models.TextField(max_length=4000, blank=True, null=True, help_text='Info block description')
    active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default='0')
    showcase = models.ForeignKey(Showcase, help_text='Showcase', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    name = models.CharField(max_length=100, help_text='Product name')
    description = models.TextField(max_length=2000, blank=True, null=True, help_text='Product description')
    price = MoneyField(help_text='Product price', max_digits=14, decimal_places=2, default=0.0, default_currency='RUB')
    unit_price = models.CharField(max_length=20, help_text='Product unit price')
    active = models.BooleanField(default=True)
    image = models.ImageField(upload_to=upload_product_image_to, blank=True)
    #    image = models.ImageField(upload_to='images/products', blank=True)
    owner = models.ForeignKey(User, help_text='Product owner', on_delete=models.SET_NULL, null=True)

    def save(self):
        super(Product, self).save()
        width = 640
        height = 480

        if self.id is not None:
            previous = Product.objects.get(id=self.id)
            if self.image and (
                    self.image != previous.image or (previous.image.width > width or previous.image.height > height)):
                image = Image.open(self.image.path)
                image = image.resize((width, height), Image.ANTIALIAS)
                image.save(self.image.path, quality=75)

    def __str__(self):
        return self.name


class Images(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    order = models.IntegerField(help_text='Field for ordering', null=True)
    image = models.ImageField(upload_to='images/products', blank=True)

    product = models.ForeignKey(Product, default=None, related_name='images', on_delete=models.CASCADE)
