# Generated by Django 2.2.1 on 2019-06-04 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uaccounts', '0001_initial'),
        ('saccounts', '0003_customerservice'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CustomerService',
            new_name='CustomerComplaint',
        ),
    ]
