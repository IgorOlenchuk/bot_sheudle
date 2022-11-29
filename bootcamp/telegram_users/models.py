from django.db import models


class TelegramUser(models.Model):

    id = models.IntegerField(unique=True, primary_key=True)
    tg_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    number = models.CharField(max_length=20)
    is_banned = models.BooleanField(default=False)
    is_push_maker = models.BooleanField(default=False)
    is_respondent = models.BooleanField(default=False)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.tg_name