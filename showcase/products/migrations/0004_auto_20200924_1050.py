# Generated by Django 2.2.7 on 2020-09-24 10:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import products.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0003_product_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, help_text='Product description', max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to=products.models.upload_to),
        ),
        migrations.CreateModel(
            name='ShowcaseInfo',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(default='New product', help_text='Product name', max_length=100)),
                ('description', models.TextField(blank=True, help_text='Product description', max_length=4000, null=True)),
                ('order', models.PositiveIntegerField(default='0')),
                ('owner', models.ForeignKey(help_text='Product owner', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
