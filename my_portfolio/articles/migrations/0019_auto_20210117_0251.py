# Generated by Django 3.1.4 on 2021-01-17 01:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0018_auto_20210117_0217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_image',
            field=models.FileField(null=True, upload_to='image', verbose_name='Image of Article'),
        ),
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 17, 2, 51, 5, 182893), verbose_name='Date'),
        ),
    ]