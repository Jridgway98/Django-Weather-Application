# Generated by Django 3.1.1 on 2020-11-05 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0007_powerplant_time_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='time_created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]