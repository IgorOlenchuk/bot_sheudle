from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('telegram_users.urls', namespace='telegram_users')),
    path('api/', include('userbot.urls', namespace='userbot')),
]
