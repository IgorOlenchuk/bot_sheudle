# Generated by Django 3.2 on 2022-11-09 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userbot', '0012_auto_20221109_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shedule',
            name='time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
