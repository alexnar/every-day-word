from django.http import HttpResponse
from django.shortcuts import render
from dict.models import TodayWord, Dictionary, UseExample, NewWord
from django.views.generic import ListView, CreateView, UpdateView
from dict.forms import NewWordForm


# Create your views here.

def index(request):
    today_word_pk = TodayWord.objects.all()[0].pk
    today_word = Dictionary.objects.get(pk=today_word_pk)
    today_word_usage = UseExample.objects.filter(word=today_word_pk)
    context = {'today_word': today_word, 'today_word_usage': today_word_usage}
    return render(request, 'dict/index.html', context)


# def new_word(request):
#     return render(request, 'dict/new_word.html', {})


class DictionaryView(ListView):
    model = Dictionary
    context_object_name = 'dictionary'
    template_name = 'dict/dicionary.html'


class CreateWordView(CreateView):
    model = NewWord
    template_name = 'dict/new_word.html'
    form_class = NewWordForm
    success_url = '/'

    def form_valid(self, form):
        word = form.save(commit=False)
        word.author = self.request.user
        return super(CreateWordView, self).form_valid(form)


class UpdateWordView(UpdateView):
    pass


