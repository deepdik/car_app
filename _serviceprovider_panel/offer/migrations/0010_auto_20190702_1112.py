# Generated by Django 2.2.1 on 2019-07-02 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0009_auto_20190702_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriptionplan',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='subscriptionplan',
            name='validity_from',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='subscriptionplan',
            name='validity_to',
            field=models.DateTimeField(),
        ),
    ]
