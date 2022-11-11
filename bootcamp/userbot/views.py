from .models import Lesson, Day_lesson, Teacher_lesson
from .serializers import LessonSerializer, Day_lessonSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


@api_view(['GET'])
def days_list_all(request):
    days = Day_lesson.objects.all()
    serializer = Day_lessonSerializer(days, many=True)
    return Response(serializer.data, status.HTTP_200_OK)

@api_view(['GET'])
def days_list(request, pk):
    days = Day_lesson.objects.filter(day=pk)
    serializer = Day_lessonSerializer(days, many=True)
    return Response(serializer.data, status.HTTP_200_OK)




@api_view(['GET'])
def lessons_list_all(request):
    lessons = Lesson.objects.all()
    serializer = LessonSerializer(lessons, many=True)
    return Response(serializer.data, status.HTTP_200_OK)

@api_view(['GET'])
def lessons_list(request, pk):
    lessons = Lesson.objects.filter(day=pk)
    serializer = LessonSerializer(lessons, many=True)
    return Response(serializer.data, status.HTTP_200_OK)