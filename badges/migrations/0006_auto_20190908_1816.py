# Generated by Django 2.2.5 on 2019-09-08 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('badges', '0005_auto_20190908_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='badge',
            name='endpoint_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='badge',
            name='refresh_interval',
            field=models.DurationField(blank=True, null=True),
        ),
    ]
