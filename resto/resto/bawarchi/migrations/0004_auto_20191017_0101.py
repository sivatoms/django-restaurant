# Generated by Django 2.2.4 on 2019-10-17 05:01

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bawarchi', '0003_auto_20191016_2350'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='Time',
            field=models.TimeField(default=datetime.datetime(2019, 10, 17, 1, 1, 12, 424795)),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='ReserveDate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
