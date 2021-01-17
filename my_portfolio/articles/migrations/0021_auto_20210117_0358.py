# Generated by Django 3.1.4 on 2021-01-17 02:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0020_auto_20210117_0302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_image',
            field=models.ImageField(blank=True, null=True, upload_to='image', verbose_name='Image of Article'),
        ),
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 17, 3, 58, 9, 346244), verbose_name='Date'),
        ),
    ]
