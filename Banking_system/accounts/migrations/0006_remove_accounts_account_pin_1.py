# Generated by Django 3.1.6 on 2021-02-05 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20210204_2244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accounts',
            name='Account_pin_1',
        ),
    ]
