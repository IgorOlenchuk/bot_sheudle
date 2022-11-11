from django.db import models


class TelegramUser(models.Model):

    id = models.IntegerField(unique=True, primary_key=True)
    tg_name = models.CharField(max_length=30)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.tg_name
