# Generated by Django 2.2.1 on 2019-07-02 07:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0005_auto_20190702_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersubscription',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 2, 11, 4, 18, 547429)),
        ),
    ]
