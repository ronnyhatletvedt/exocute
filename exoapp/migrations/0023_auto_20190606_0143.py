# Generated by Django 2.2.1 on 2019-06-06 01:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exoapp', '0022_shipment_departure_airport'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shipment',
            old_name='departure_airport',
            new_name='destination_airport',
        ),
    ]
