# Generated by Django 2.2.1 on 2019-07-04 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uaccounts', '0005_auto_20190625_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registereduser',
            name='user_type',
            field=models.CharField(choices=[('1', 'User'), ('2', 'Service Provider'), ('3', 'Both')], max_length=20),
        ),
    ]
