# Generated by Django 3.2 on 2022-11-02 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlackList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=150, verbose_name='ID в телеграмм')),
                ('user_name', models.CharField(max_length=150, unique=True, verbose_name='Username в телеграмм')),
                ('is_bot', models.BooleanField(default=False, verbose_name='Бот')),
            ],
            options={
                'ordering': ('-user_name',),
            },
        ),
        migrations.CreateModel(
            name='ChatHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('messages_id', models.IntegerField(blank=True, null=True)),
                ('chat', models.CharField(blank=True, max_length=150, null=True)),
                ('userbot', models.CharField(blank=True, max_length=150, null=True, verbose_name='Юзербот')),
                ('user_id', models.CharField(blank=True, max_length=150, null=True)),
                ('user_fullname', models.CharField(blank=True, max_length=150, null=True, verbose_name='Имя пользователя')),
                ('text', models.CharField(blank=True, max_length=150, null=True)),
                ('animation', models.CharField(blank=True, max_length=150, null=True)),
                ('sticker', models.CharField(blank=True, max_length=150, null=True)),
                ('photo', models.CharField(blank=True, max_length=150, null=True)),
                ('audio', models.CharField(blank=True, max_length=150, null=True)),
                ('document', models.CharField(blank=True, max_length=150, null=True)),
                ('video', models.CharField(blank=True, max_length=150, null=True)),
                ('voice', models.CharField(blank=True, max_length=150, null=True)),
                ('date', models.DateTimeField(blank=True, null=True, verbose_name='Дата сообщения')),
            ],
            options={
                'verbose_name': 'История чата',
                'verbose_name_plural': 'истории чатов',
                'ordering': ('-date',),
            },
        ),
        migrations.CreateModel(
            name='Proxy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scheme', models.CharField(blank=True, max_length=150, null=True)),
                ('hostname', models.CharField(max_length=150)),
                ('port', models.CharField(max_length=150)),
                ('username', models.CharField(max_length=150)),
                ('password', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Прокси',
                'verbose_name_plural': 'прокси',
            },
        ),
        migrations.CreateModel(
            name='UserBot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tg_name', models.CharField(blank=True, max_length=150, null=True, verbose_name='Имя в телеграмм')),
                ('api_id', models.CharField(max_length=150)),
                ('api_hash', models.CharField(max_length=150)),
                ('proxy', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='userbot.proxy')),
            ],
            options={
                'verbose_name': 'Юзербот',
                'verbose_name_plural': 'юзерботы',
            },
        ),
        migrations.CreateModel(
            name='Chats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_username', models.CharField(max_length=150, verbose_name='Наименование чата/группы')),
                ('chat_id', models.IntegerField()),
                ('notification', models.CharField(default='me', max_length=150, verbose_name='Куда отправять уведомления')),
                ('is_running', models.BooleanField(default=False, verbose_name='Работает')),
                ('blacklist', models.ManyToManyField(blank=True, null=True, to='userbot.BlackList')),
                ('userbot', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='userbot.userbot', verbose_name='Юзербот')),
            ],
            options={
                'verbose_name': 'Чат',
                'verbose_name_plural': 'чаты',
            },
        ),
    ]
