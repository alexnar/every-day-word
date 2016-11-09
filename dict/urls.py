from django.conf.urls import url
from . import views
from dict.views import DictionaryView

urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'new_word',views.new_word, name='new_word'),
    url(r'dictionary', DictionaryView.as_view(), name='dict_view'),
]