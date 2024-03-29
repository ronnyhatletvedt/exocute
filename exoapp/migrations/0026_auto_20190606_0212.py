# Generated by Django 2.2.1 on 2019-06-06 02:12

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exoapp', '0025_auto_20190606_0146'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('name_short', models.CharField(blank=True, default=None, help_text='The day to day name of the customer.', max_length=100, null=True)),
                ('name_official', models.CharField(blank=True, default=None, help_text='The official name of the customer.', max_length=100, null=True)),
                ('class_1', models.IntegerField(blank=True, default=None, help_text='First internal classification.', null=True)),
                ('class_2', models.IntegerField(blank=True, default=None, help_text='Second internal classification.', null=True)),
                ('created', models.DateTimeField(default=datetime.datetime.now, verbose_name='created')),
                ('updated', models.DateTimeField(default=datetime.datetime.now, verbose_name='updated')),
                ('iso_country', models.ForeignKey(blank=True, default=None, help_text='Official country code of the airport.', null=True, on_delete=django.db.models.deletion.CASCADE, to='exoapp.Country')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerDestination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipment_address', models.CharField(blank=True, default=None, help_text='Official name of the airport', max_length=255, null=True)),
                ('invoice_address', models.CharField(blank=True, default=None, help_text='Official name of the airport', max_length=255, null=True)),
                ('created', models.DateTimeField(default=datetime.datetime.now, verbose_name='created')),
                ('updated', models.DateTimeField(default=datetime.datetime.now, verbose_name='updated')),
                ('customer_id', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='exoapp.Customer')),
            ],
        ),
        migrations.RemoveField(
            model_name='baseorder',
            name='customer_id',
        ),
        migrations.RemoveField(
            model_name='order',
            name='customer_id',
        ),
        migrations.RemoveField(
            model_name='shipment',
            name='destination_airport',
        ),
        migrations.CreateModel(
            name='CustomerDestinationAirport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank_1', models.IntegerField(blank=True, default=None, help_text='Ranked on convenience.', null=True)),
                ('rank_2', models.IntegerField(blank=True, default=None, help_text='Ranked on availability.', null=True)),
                ('created', models.DateTimeField(default=datetime.datetime.now, verbose_name='created')),
                ('updated', models.DateTimeField(default=datetime.datetime.now, verbose_name='updated')),
                ('customer_destination_id', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='exoapp.CustomerDestination')),
                ('destination_airport', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='exoapp.Airport')),
            ],
        ),
        migrations.AddField(
            model_name='baseorder',
            name='customer_destination_airport_id',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='exoapp.CustomerDestinationAirport'),
        ),
        migrations.AddField(
            model_name='order',
            name='customer_destination_airport_id',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='exoapp.CustomerDestinationAirport'),
        ),
    ]
