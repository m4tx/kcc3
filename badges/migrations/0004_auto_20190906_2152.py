# Generated by Django 2.2.5 on 2019-09-06 21:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('badges', '0003_auto_20190908_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='badge',
            name='owners',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='badge',
            name='players',
            field=models.ManyToManyField(blank=True, to='common.Player'),
        ),
    ]
