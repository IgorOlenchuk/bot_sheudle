from django.db import models
from django.utils import timezone


class Teacher_lesson(models.Model):

    teacher = models.CharField(max_length=150, null=True, blank=True, verbose_name='Учитель')
    comments = models.CharField(max_length=150, null=True, blank=True, verbose_name='Комментарий')
    
    class Meta:
        ordering = ('teacher',)
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'

    def __str__(self):
        return self.teacher


class Lesson(models.Model):

    lesson = models.CharField(max_length=50, verbose_name='Урок', null=True, blank=True)
    teacher = models.ForeignKey(Teacher_lesson, on_delete=models.CASCADE)
    comments = models.CharField(max_length=150, null=True, blank=True, verbose_name='Комментарий')
    
    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'

    def __str__(self):
        return f'{self.lesson},{self.teacher},{self.comments}'


class Day_lesson(models.Model):
    
    DAYS = [('Mn', 'Понедельник'), ('Tu', 'Вторник'), ('We', 'Среда'), ('Th', 'Четверг'), ('Fr', 'Пятница')]
    day =models.CharField(max_length=10, choices=DAYS, null=True, blank=True)
    time_from = models.TimeField(null=True, blank=True)
    time_to = models.TimeField(null=True, blank=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    class Meta:
        ordering = ('time_from',)
        verbose_name = 'День недели'
        verbose_name_plural = 'Дни недели'

    def __str__(self):
        return self.day


class Question(models.Model):
    
    message_id = models.IntegerField(null=True, blank=True)
    tg_name = models.CharField(max_length=30, null=True, blank=True)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    number = models.CharField(max_length=20, null=True, blank=True)
    question = models.CharField(max_length=3000, verbose_name='Вопрос', null=True, blank=True)
    question_date = models.DateTimeField(default=timezone.now, verbose_name='Дата вопроса', db_index=True, null=True, blank=True)
    answered = models.BooleanField(default=False, verbose_name='Ответ', null=True, blank=True)


    class Meta:
        ordering = ('question_date',)
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __int__(self):
        return self.message_id


class Answer(models.Model):
    
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=3000, verbose_name='Ответ')
    answer_date = models.DateTimeField(default=timezone.now, verbose_name='Дата ответа', db_index=True)


    class Meta:
        ordering = ('answer_date',)
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

    def __str__(self):
        return self.answer
