# Generated by Django 2.2 on 2021-10-22 14:49

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slotbooking', '0010_auto_20211022_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slotbooking',
            name='user',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name=django.contrib.auth.models.User),
        ),
    ]
