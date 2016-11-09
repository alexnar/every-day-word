from django.contrib import admin
from dict.models import Dictionary, TodayWord, UseExample

# Register your models here.

admin.site.register(Dictionary)
admin.site.register(TodayWord)
admin.site.register(UseExample)