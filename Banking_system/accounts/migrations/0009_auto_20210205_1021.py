# Generated by Django 3.1.6 on 2021-02-05 18:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20210205_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='date_opened',
            field=models.DateField(default=datetime.datetime(2021, 2, 5, 18, 21, 1, 882018, tzinfo=utc), verbose_name='date'),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='email',
            field=models.EmailField(max_length=200, unique=True),
        ),
    ]