# Generated by Django 2.2.1 on 2019-05-29 03:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exoapp', '0003_auto_20190529_0344'),
    ]

    operations = [
        migrations.CreateModel(
            name='AirportClass',
            fields=[
                ('iata_code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(default=datetime.datetime.now, verbose_name='created')),
                ('updated', models.DateTimeField(default=datetime.datetime.now, verbose_name='updated')),
            ],
        ),
    ]
