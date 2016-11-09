from django.db import models


class Dictionary(models.Model):
    word = models.CharField(max_length=75)
    definition = models.CharField(max_length=512)
    author = models.CharField(max_length=128, default="everydayword.ru")
    rating = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.word


class UseExample(models.Model):
    word = models.ForeignKey(Dictionary, null=True)
    use_example = models.CharField(max_length=1024)

    def __str__(self):
        return self.use_example[:20] + "..."


class TodayWord(models.Model):
    today_word = models.ForeignKey(Dictionary)

    def __str__(self):
        return self.today_word.word
