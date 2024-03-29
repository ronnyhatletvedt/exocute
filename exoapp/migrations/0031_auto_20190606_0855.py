# Generated by Django 2.2.1 on 2019-06-06 08:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exoapp', '0030_auto_20190606_0441'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Shipment',
            new_name='CustomerShipment',
        ),
        migrations.RenameModel(
            old_name='OrderLine',
            new_name='ShipmentLine',
        ),
        migrations.RemoveField(
            model_name='order',
            name='customer_destination_airport_id',
        ),
        migrations.AddField(
            model_name='order',
            name='customer_destination_id',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='exoapp.CustomerDestination'),
        ),
        migrations.AlterField(
            model_name='baseorder',
            name='customer_destination_id',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='exoapp.CustomerDestination'),
        ),
    ]
