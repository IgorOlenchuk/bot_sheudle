from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import TelegramUserSerializerGet, TelegramUserSerializerPost
from .models import TelegramUser


@api_view(['POST'])
def user_post(request):
    serializer = TelegramUserSerializerPost(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def user_get(request, pk):
    user = get_object_or_404(TelegramUser, pk=pk)
    serializer = TelegramUserSerializerGet(user)
    return Response(serializer.data)


@api_view(['GET'])
def user_ids_list(request):
    users = TelegramUser.objects.all()
    return Response(data=users.values_list('id', flat=True))
