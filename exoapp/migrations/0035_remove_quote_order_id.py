# Generated by Django 2.2.1 on 2019-06-06 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exoapp', '0034_auto_20190606_0913'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quote',
            name='order_id',
        ),
    ]
