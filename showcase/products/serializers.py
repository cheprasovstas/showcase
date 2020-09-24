from django.contrib.auth.models import User, Group
from rest_framework import serializers
from products.models import Product, Images


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id',
                  'name',
                  'description',
                  'price',
                  )