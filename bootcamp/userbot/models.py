from django.db import models


class Teacher_lesson(models.Model):

    teacher = models.CharField(max_length=150, null=True, blank=True, verbose_name='Учитель')
    comments = models.CharField(max_length=150, null=True, blank=True, verbose_name='Комментарий')
    
    class Meta:
        ordering = ('teacher',)
        verbose_name = 'Учителя'

    def __str__(self):
        return self.teacher

class Lesson(models.Model):

    lesson = models.CharField(max_length=50, verbose_name='Урок', null=True, blank=True)
    teacher = models.ForeignKey(Teacher_lesson, on_delete=models.CASCADE)
    comments = models.CharField(max_length=150, null=True, blank=True, verbose_name='Комментарий')
    
    class Meta:
        verbose_name = 'Предметы'

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

    def __str__(self):
        return self.day
