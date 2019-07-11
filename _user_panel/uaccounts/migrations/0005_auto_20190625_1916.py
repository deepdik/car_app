# Generated by Django 2.2.1 on 2019-06-25 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uaccounts', '0004_temporaryotp_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registereduser',
            name='is_active',
        ),
        migrations.AddField(
            model_name='registereduser',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
    ]
