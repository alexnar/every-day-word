from django.conf.urls import url, include
from django.contrib.auth import views
import accounts.views

urlpatterns = [
    url(r'login/', views.login, {'template_name': 'accounts/login.html'}, name='login'),
    url(r'logout/', views.logout, {'next_page': '/'}),
    url(r'register/', accounts.views.register, name='register')

]