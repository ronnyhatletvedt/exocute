# Generated by Django 2.2.1 on 2019-05-31 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exoapp', '0011_auto_20190531_0452'),
    ]

    operations = [
        migrations.AddField(
            model_name='nasdaqindex',
            name='distribution',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='nasdaqindex',
            name='standard_deviation',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=4, null=True),
        ),
    ]
