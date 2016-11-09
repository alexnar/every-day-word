from django.db import models


class Dictionary(models.Model):
    word = models.CharField(max_length=75)
    definition = models.CharField(max_length=512)

    def __str__(self):
        return self.word


class TodayWord(models.Model):
    today_word = models.ForeignKey(Dictionary)

    def __str__(self):
        return self.today_word.word
