# Generated by Django 2.2.1 on 2019-05-29 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exoapp', '0006_nasdaqindexclass_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='nasdaqindexclass',
            name='standard_deviation',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4),
        ),
        migrations.AddField(
            model_name='nasdaqindexclass',
            name='volume',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=7),
        ),
    ]
