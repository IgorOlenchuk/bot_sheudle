from rest_framework import serializers

from .models import TelegramUser


class TelegramUserSerializerGet(serializers.ModelSerializer):

    class Meta:
        model = TelegramUser
        fields = ('id', 'tg_name', 'first_name', 'last_name',
                  'number', 'is_banned', 'is_push_maker', 'is_respondent')


class TelegramUserSerializerPost(serializers.ModelSerializer):

    class Meta:
        model = TelegramUser
        fields = ('id', 'tg_name', 'first_name', 'last_name', 'number')