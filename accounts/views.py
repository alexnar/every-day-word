from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.contrib import auth
#from django.contrib.auth.forms import UserCreationForm
from accounts.forms import RegisterForm


# Create your views here.
# this login required decorator is to not allow to any
# view without authenticating


def register(request):
    context = {}
    context.update(csrf(request))
    context['form'] = RegisterForm()
    if request.POST:
        new_user_form = RegisterForm(request.POST)
        if new_user_form.is_valid():
            new_user_form.save()
            new_user = auth.authenticate(username=new_user_form.cleaned_data['username'],
                                         password=new_user_form.cleaned_data['password1'])
            auth.login(request, new_user)
            return redirect('/')
        else:
            context['form'] = new_user_form
    return render(request, 'accounts/register.html', context)
