# Generated by Django 4.2.7 on 2023-11-24 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FlashDS', '0002_request_pickup_address_request_pickup_lat_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='pickup_name',
            field=models.CharField(blank=True, max_length=45),
        ),
    ]
