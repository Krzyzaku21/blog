# Generated by Django 3.1.4 on 2021-01-17 16:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0025_auto_20210117_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 17, 17, 1, 50, 763522), verbose_name='Date'),
        ),
    ]
