# Generated by Django 2.2.1 on 2019-06-06 01:15

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exoapp', '0019_baseorder'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseOrderLines',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weekday', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('volume', models.IntegerField(blank=True, default=None, help_text='The base order volume (in boxes) for the given `weight_class`.', null=True)),
                ('created', models.DateTimeField(default=datetime.datetime.now, verbose_name='created')),
                ('updated', models.DateTimeField(default=datetime.datetime.now, verbose_name='updated')),
                ('base_order_id', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='exoapp.BaseOrder')),
                ('weight_class', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='exoapp.WeightClass')),
            ],
        ),
    ]
