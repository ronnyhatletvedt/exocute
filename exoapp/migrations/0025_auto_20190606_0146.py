# Generated by Django 2.2.1 on 2019-06-06 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exoapp', '0024_auto_20190606_0144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderline',
            name='volume',
            field=models.IntegerField(blank=True, default=None, help_text='The order line volume (in boxes) for the given `weight_class`.', null=True),
        ),
    ]
