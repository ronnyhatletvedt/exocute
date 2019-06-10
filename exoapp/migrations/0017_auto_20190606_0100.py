# Generated by Django 2.2.1 on 2019-06-06 01:00

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exoapp', '0016_auto_20190606_0045'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('iso_country', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('country', models.CharField(blank=True, default=None, help_text='The official name of the country.', max_length=50, null=True)),
                ('continent_id', models.CharField(blank=True, default=None, help_text='A unique id for the continent.', max_length=10, null=True)),
                ('north', models.DecimalField(blank=True, decimal_places=10, default=None, help_text='The northern latitide of the country.', max_digits=13, null=True)),
                ('south', models.DecimalField(blank=True, decimal_places=10, default=None, help_text='The southern latitide of the country.', max_digits=13, null=True)),
                ('west', models.DecimalField(blank=True, decimal_places=10, default=None, help_text='The western longitude of the country.', max_digits=13, null=True)),
                ('east', models.DecimalField(blank=True, decimal_places=10, default=None, help_text='The eastern longitude of the country.', max_digits=13, null=True)),
                ('class_1', models.IntegerField(blank=True, default=None, help_text='First internal classification.', null=True)),
                ('class_2', models.IntegerField(blank=True, default=None, help_text='Second internal classification.', null=True)),
                ('created', models.DateTimeField(default=datetime.datetime.now, verbose_name='created')),
                ('updated', models.DateTimeField(default=datetime.datetime.now, verbose_name='updated')),
            ],
        ),
        migrations.RemoveField(
            model_name='airportclass',
            name='continent',
        ),
        migrations.AlterField(
            model_name='airportclass',
            name='iso_country',
            field=models.ForeignKey(help_text='Official country code of the airport.', on_delete=django.db.models.deletion.CASCADE, to='exoapp.Country'),
        ),
    ]
