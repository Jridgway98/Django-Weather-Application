# Generated by Django 3.1.1 on 2020-11-05 05:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0010_auto_20201105_0511'),
    ]

    operations = [
        migrations.RenameField(
            model_name='city',
            old_name='sensor_locatiion',
            new_name='sensor_location',
        ),
    ]
