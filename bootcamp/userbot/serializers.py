from rest_framework import serializers

from .models import Lesson, Teacher_lesson, Day_lesson


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = ('__all__')


class Day_lessonSerializer(serializers.ModelSerializer):
    lesson = serializers.StringRelatedField(read_only=True)
    comments = LessonSerializer(many=True, read_only=True)
    class Meta:
        model = Day_lesson
        fields = ('day', 'time_from', 'time_to', 'lesson', 'comments')        