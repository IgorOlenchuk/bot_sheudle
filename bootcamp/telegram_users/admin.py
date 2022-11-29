from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import TelegramUser


class TelegramUserAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'tg_name', 'first_name', 'last_name',
                       'number', )
    list_display = ('id', 'tg_name', 'first_name', 'last_name',
                    'number', 'is_banned', 'is_push_maker', 'is_respondent')


admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(TelegramUser, TelegramUserAdmin)