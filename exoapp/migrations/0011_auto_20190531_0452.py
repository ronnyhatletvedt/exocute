# Generated by Django 2.2.1 on 2019-05-31 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exoapp', '0010_auto_20190531_0445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nasdaqindex',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=5, null=True),
        ),
    ]