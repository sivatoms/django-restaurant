# Generated by Django 2.2.4 on 2019-10-18 00:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bawarchi', '0005_auto_20191017_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='ReserveDate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='Time',
            field=models.TimeField(default=datetime.datetime(2019, 10, 17, 20, 17, 29, 786028)),
        ),
    ]
