# Generated by Django 3.2 on 2022-11-09 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userbot', '0013_alter_shedule_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Day_lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('Moday', 'Понедельник'), ('Tuesday', 'Вторник'), ('Wethday', 'Среда'), ('chetverg', 'Четверг'), ('Fryday', 'Пятница')], max_length=10)),
            ],
            options={
                'verbose_name': 'День недели',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson', models.CharField(max_length=50, verbose_name='Урок')),
                ('comments', models.CharField(blank=True, max_length=150, null=True, verbose_name='Комментарий')),
                ('day', models.ManyToManyField(to='userbot.Day_lesson')),
            ],
            options={
                'verbose_name': 'Предметы',
            },
        ),
        migrations.CreateModel(
            name='Teacher_lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher', models.CharField(blank=True, max_length=150, null=True, verbose_name='Учитель')),
                ('comments', models.CharField(blank=True, max_length=150, null=True, verbose_name='Комментарий')),
            ],
            options={
                'verbose_name': 'Учителя',
                'ordering': ('teacher',),
            },
        ),
        migrations.CreateModel(
            name='Time_lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Время урока',
                'ordering': ('time',),
            },
        ),
        migrations.DeleteModel(
            name='Shedule',
        ),
        migrations.AddField(
            model_name='lesson',
            name='teacher',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='userbot.teacher_lesson'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='time',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='userbot.time_lesson'),
        ),
    ]
