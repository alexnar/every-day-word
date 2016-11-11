from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from dict.models import TodayWord, Dictionary, UseExample, NewWord, ImageExampleModel
from django.views.generic import ListView, CreateView, UpdateView, FormView
from dict.forms import NewWordForm, ImageExampleForm


# Create your views here.

def index(request):
    today_word = TodayWord.objects.all()[0].today_word
    today_word_usage = UseExample.objects.filter(word=today_word)
    img = ImageExampleModel.objects.all()
    context = {'today_word': today_word, 'today_word_usage': today_word_usage, 'img': img}
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


class ImageExampleView(FormView):
    template_name = 'dict/image_upload.html'
    form_class = ImageExampleForm
    success_url = '/'

    def form_valid(self, form):
        image = ImageExampleModel(img=self.get_form_kwargs().get('files')['img'])
        image.save()
        return super(ImageExampleView, self).form_valid(form)

