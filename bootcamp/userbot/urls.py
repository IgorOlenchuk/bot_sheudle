from django.urls import path

from .views import lessons_list_all, lessons_list, days_list_all, days_list, userquestion_post, useranswer_post

app_name = 'userbot'


urlpatterns = [
    path('days/', days_list_all, name='days_list_all'),
    path('days/<str:pk>/lessons/', days_list, name='days_list'),
    path('lessons/', lessons_list_all, name='lessons_list_all'),
    path('lessons/<int:pk>/days/', lessons_list, name='lessons_list'),
    path('questions/<int:pk>/', userquestion_post, name='userquestion_post'),
    path('questions/<int:pk>/answer/<int:question_id>/', useranswer_post, name='useranswer_post'),
]
