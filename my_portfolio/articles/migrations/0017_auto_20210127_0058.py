# Generated by Django 3.1.4 on 2021-01-26 23:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0016_auto_20210127_0055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 27, 0, 58, 15, 506996), verbose_name='Date'),
        ),
    ]
