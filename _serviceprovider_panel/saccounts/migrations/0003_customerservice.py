# Generated by Django 2.2.1 on 2019-06-04 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uaccounts', '0001_initial'),
        ('saccounts', '0002_auto_20190603_1339'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint', models.CharField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='csuser', to='uaccounts.RegisteredUser')),
            ],
        ),
    ]
