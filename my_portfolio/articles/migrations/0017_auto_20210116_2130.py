# Generated by Django 3.1.4 on 2021-01-16 20:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0016_auto_20210116_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_image',
            field=models.ImageField(null=True, upload_to='images', verbose_name='Image of Article'),
        ),
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 16, 21, 30, 30, 35469), verbose_name='Date'),
        ),
    ]
