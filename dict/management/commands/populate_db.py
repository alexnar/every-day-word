from django.core.management.base import BaseCommand
from dict.models import Dictionary
import csv
import os


class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'our help string comes here'

    @staticmethod
    def _create_tags():
        module_dir = os.path.dirname(__file__)
        file_path = os.path.join(module_dir, 'parse_words/dict.csv')
        for key, val in csv.reader(open(file_path, "r")):
            dictionary_row = Dictionary(word=key, definition=val)
            dictionary_row.save()

    def handle(self, *args, **options):
        self._create_tags()
