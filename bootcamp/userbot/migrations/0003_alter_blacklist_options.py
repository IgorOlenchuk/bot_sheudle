# Generated by Django 3.2 on 2022-11-02 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userbot', '0002_blacklist_date_add'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blacklist',
            options={'ordering': ('-date_add',)},
        ),
    ]
