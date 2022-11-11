from django.urls import path

from .views import lessons_list_all, lessons_list, days_list_all, days_list

app_name = 'userbot'


urlpatterns = [
    path('days/', days_list_all, name='days_list_all'),
    path('days/<str:pk>/lessons/', days_list, name='days_list'),
    path('lessons/', lessons_list_all, name='lessons_list_all'),
    path('lessons/<int:pk>/days/', lessons_list, name='lessons_list'),
]
