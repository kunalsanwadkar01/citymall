# Generated by Django 2.2 on 2021-10-22 09:41

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slotbooking', '0002_auto_20211018_0026'),
    ]

    operations = [
        migrations.AddField(
            model_name='slotbooking',
            name='user',
            field=models.CharField(max_length=100, null=True, verbose_name=django.contrib.auth.models.User),
        ),
    ]
