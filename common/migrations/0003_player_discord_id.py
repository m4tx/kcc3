# Generated by Django 2.2.5 on 2019-09-14 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_player_usma_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='discord_id',
            field=models.CharField(max_length=30, null=True),
        ),
    ]