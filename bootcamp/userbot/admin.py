from django.contrib import admin

from .models import Lesson, Teacher_lesson, Day_lesson


@admin.register(Teacher_lesson)
class Teacher_lessonAdmin(admin.ModelAdmin):
    list_display = ('teacher',)
    list_filter = ('teacher',)
    search_fields = ('teacher',)


@admin.register(Day_lesson)
class Day_lessonAdmin(admin.ModelAdmin):
    list_display = ('day', 'time_from', 'time_to', 'lesson')
    list_filter = ('day',)
    search_fields = ('day',)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('lesson', 'comments')
    list_filter = ('lesson', 'teacher')
    search_fields = ('lesson',)

