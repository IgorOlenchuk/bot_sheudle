from django.urls import path

from .views import user_post, user_get, user_ids_list, user_respondents_list

app_name = 'telegram_users'


urlpatterns = [
    path('users/', user_post, name='user_post'),
    path('users/ids/', user_ids_list, name='user_ids_list'),
    path('users/respondents/', user_respondents_list,
         name='user_respondents_list'),
    path('users/<int:pk>/', user_get, name='user_get'),
]