# Generated by Django 2.2.1 on 2019-06-03 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('uaccounts', '0001_initial'),
        ('saccounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userreview',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rvuser', to='uaccounts.RegisteredUser'),
        ),
        migrations.AddField(
            model_name='subcategorymanager',
            name='garage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scm_garage', to='saccounts.Garage'),
        ),
        migrations.AddField(
            model_name='subcategorymanager',
            name='subcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scm_subcategory', to='saccounts.ServiceSubType'),
        ),
        migrations.AddField(
            model_name='servicesubtype',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='saccounts.ServiceType'),
        ),
        migrations.AddField(
            model_name='garage',
            name='service_subtype',
            field=models.ManyToManyField(related_name='gsst', through='saccounts.SubCategoryManager', to='saccounts.ServiceSubType'),
        ),
        migrations.AddField(
            model_name='garage',
            name='service_type',
            field=models.ManyToManyField(related_name='gst', through='saccounts.CategoryManager', to='saccounts.ServiceType'),
        ),
        migrations.AddField(
            model_name='garage',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='guser', to='uaccounts.RegisteredUser'),
        ),
        migrations.AddField(
            model_name='categorymanager',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cm_category', to='saccounts.ServiceType'),
        ),
        migrations.AddField(
            model_name='categorymanager',
            name='garage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cm_garage', to='saccounts.Garage'),
        ),
        migrations.AlterUniqueTogether(
            name='subcategorymanager',
            unique_together={('garage', 'subcategory')},
        ),
        migrations.AlterUniqueTogether(
            name='categorymanager',
            unique_together={('garage', 'category')},
        ),
    ]
