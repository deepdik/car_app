# Generated by Django 2.2.1 on 2019-06-21 06:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('saccounts', '0009_auto_20190620_0847'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicetype',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
