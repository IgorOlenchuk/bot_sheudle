# Generated by Django 3.2 on 2022-11-09 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userbot', '0018_auto_20221109_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userbot.teacher_lesson'),
        ),
    ]
