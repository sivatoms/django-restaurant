# Generated by Django 2.2.4 on 2019-10-18 00:18

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bawarchi', '0006_auto_20191017_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='ReserveDate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='Time',
            field=models.TimeField(default=datetime.datetime(2019, 10, 17, 20, 18, 5, 336060)),
        ),
    ]
