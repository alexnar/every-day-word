from django.conf.urls import url
from . import views
from dict.views import DictionaryView, CreateWordView, ImageExampleView

urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'new_word',CreateWordView.as_view(), name='new_word'),
    url(r'dictionary', DictionaryView.as_view(), name='dict_view'),
    url(r'image_upload', ImageExampleView.as_view(), name='image_upload'),
]