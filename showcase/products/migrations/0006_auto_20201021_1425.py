# Generated by Django 2.2.16 on 2020-10-21 11:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0005_auto_20201019_2015'),
    ]

    operations = [
        migrations.AddField(
            model_name='showcaseinfo',
            name='owner',
            field=models.ForeignKey(help_text='Owner', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='showcaseinfo',
            name='showcase',
            field=models.ForeignKey(help_text='Showcase', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='showcaseinfo', to='products.Showcase'),
        ),
    ]