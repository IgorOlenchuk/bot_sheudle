# Generated by Django 3.2 on 2022-11-15 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userbot', '0028_question_message_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='message_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]