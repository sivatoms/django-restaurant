# Generated by Django 2.2.4 on 2019-10-18 00:15

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bawarchi', '0004_auto_20191017_0101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='ReserveDate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='Time',
            field=models.TimeField(default=datetime.datetime(2019, 10, 17, 20, 15, 45, 927092)),
        ),
    ]
