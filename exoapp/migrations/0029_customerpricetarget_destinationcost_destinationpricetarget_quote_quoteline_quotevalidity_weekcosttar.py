# Generated by Django 2.2.1 on 2019-06-06 02:53

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exoapp', '0028_auto_20190606_0216'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target_week', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('created', models.DateTimeField(default=datetime.datetime.now, verbose_name='created')),
                ('updated', models.DateTimeField(default=datetime.datetime.now, verbose_name='updated')),
                ('customer_destination_id', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='exoapp.CustomerDestination')),
                ('order_id', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='exoapp.Order')),
            ],
        ),
        migrations.CreateModel(
            name='WeekPriceTarget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=5, null=True)),
                ('created', models.DateTimeField(default=datetime.datetime.now, verbose_name='created')),
                ('updated', models.DateTimeField(default=datetime.datetime.now, verbose_name='updated')),
                ('weight_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exoapp.WeightClass')),
            ],
        ),
        migrations.CreateModel(
            name='WeekCostTarget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('cost', models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=5, null=True)),
                ('created', models.DateTimeField(default=datetime.datetime.now, verbose_name='created')),
                ('updated', models.DateTimeField(default=datetime.datetime.now, verbose_name='updated')),
                ('weight_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exoapp.WeightClass')),
            ],
        ),
        migrations.CreateModel(
            name='QuoteValidity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('validity', models.IntegerField(blank=True, default=None, help_text='The timespan the quote is valid.', null=True)),
                ('created', models.DateTimeField(default=datetime.datetime.now, verbose_name='created')),
                ('updated', models.DateTimeField(default=datetime.datetime.now, verbose_name='updated')),
                ('quote_id', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='exoapp.Quote')),
            ],
        ),
        migrations.CreateModel(
            name='QuoteLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=5, null=True)),
                ('class_1', models.IntegerField(blank=True, default=None, help_text='Quote or counteroffer (ask).', null=True)),
                ('status', models.IntegerField(blank=True, default=None, help_text='Internal grading until closed.', null=True)),
                ('created', models.DateTimeField(default=datetime.datetime.now, verbose_name='created')),
                ('updated', models.DateTimeField(default=datetime.datetime.now, verbose_name='updated')),
                ('quote_id', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='exoapp.Quote')),
                ('weight_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exoapp.WeightClass')),
            ],
        ),
        migrations.CreateModel(
            name='DestinationPriceTarget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_relative', models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=5, null=True)),
                ('created', models.DateTimeField(default=datetime.datetime.now, verbose_name='created')),
                ('updated', models.DateTimeField(default=datetime.datetime.now, verbose_name='updated')),
                ('destination_airport', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='exoapp.Airport')),
                ('weight_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exoapp.WeightClass')),
            ],
        ),
        migrations.CreateModel(
            name='DestinationCost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=5, null=True)),
                ('created', models.DateTimeField(default=datetime.datetime.now, verbose_name='created')),
                ('updated', models.DateTimeField(default=datetime.datetime.now, verbose_name='updated')),
                ('destination_airport', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='exoapp.Airport')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerPriceTarget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_relative', models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=5, null=True)),
                ('created', models.DateTimeField(default=datetime.datetime.now, verbose_name='created')),
                ('updated', models.DateTimeField(default=datetime.datetime.now, verbose_name='updated')),
                ('customer_destination_id', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='exoapp.CustomerDestination')),
                ('weight_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exoapp.WeightClass')),
            ],
        ),
    ]
