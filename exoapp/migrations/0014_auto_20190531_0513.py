# Generated by Django 2.2.1 on 2019-05-31 05:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exoapp', '0013_auto_20190531_0512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nasdaqindex',
            name='weight_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exoapp.WeightClass'),
        ),
    ]
