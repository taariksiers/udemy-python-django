from django.shortcuts import render
from django.http import HttpResponse
from appTwo.models import User


def index(request) -> HttpResponse:
    return render(request, 'appTwo/index.html')


def help_me(request):
    my_dict = {'help_insert': 'Now I am coming from appTwo/help_me.html'}
    return render(request, 'appTwo/help_me.html', context=my_dict)


def users(request):
    user_list = {'users': User.objects.order_by('email')}
    return render(request, 'first_app/users.html', context=user_list)
