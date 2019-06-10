# Generated by Django 2.2.1 on 2019-06-06 02:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exoapp', '0026_auto_20190606_0212'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipment',
            name='departure_airport',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='exoapp.Airport'),
        ),
    ]