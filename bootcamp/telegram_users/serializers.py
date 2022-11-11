from rest_framework import serializers

from .models import TelegramUser


class TelegramUserSerializerGet(serializers.ModelSerializer):

    class Meta:
        model = TelegramUser
        fields = ('id', 'tg_name')


class TelegramUserSerializerPost(serializers.ModelSerializer):

    class Meta:
        model = TelegramUser
        fields = ('id', 'tg_name')
