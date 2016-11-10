from django.contrib import admin
from dict.models import Dictionary, TodayWord, UseExample, NewWord


def approve_words(modeladmin, request, word_set):
    for word in word_set:
        dictionary = Dictionary(word=word.word, definition=word.definition, author=word.author)
        dictionary.save()
        word.delete()


class NewWordAdmin(admin.ModelAdmin):
    list_display = ['word', 'definition', 'author']
    actions = [approve_words]


class DictionaryAdmin(admin.ModelAdmin):
    list_display = ['word', 'definition', 'author']


admin.site.register(NewWord, NewWordAdmin)
admin.site.register(Dictionary, DictionaryAdmin)
admin.site.register(TodayWord)
admin.site.register(UseExample)
