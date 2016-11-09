from django.core.management.base import BaseCommand
from dict.models import Dictionary, TodayWord
from random import randint


# This command would run every day. It will achieved with crontab on server
# example: * * * * * /path/to/env/bin/python3.4 /path/to/project/folder/manage.py chose_new_word

class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'our help string comes here'

    # TODO: Изменить способ выбора слов. (сейчас простой рандом)
    @staticmethod
    def _create_tags():
        count = Dictionary.objects.all().__len__()
        random_index = randint(0, count - 1)
        TodayWord.objects.all().delete()
        today_word = TodayWord(today_word=Dictionary.objects.all()[random_index])
        today_word.save()

    def handle(self, *args, **options):
        self._create_tags()
