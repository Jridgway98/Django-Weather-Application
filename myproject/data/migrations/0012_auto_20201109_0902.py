# Generated by Django 3.1.1 on 2020-11-09 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0011_auto_20201105_0526'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'ordering': ('name',)},
        ),
    ]
