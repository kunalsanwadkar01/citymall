# Generated by Django 2.2 on 2021-10-23 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slotbooking', '0015_auto_20211023_1936'),
    ]

    operations = [
        migrations.AddField(
            model_name='slotbooking',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
