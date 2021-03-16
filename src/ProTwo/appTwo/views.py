from django.shortcuts import render
from django.http import HttpResponse


def index(request) -> HttpResponse:
    return HttpResponse("<em>My Second Project</em>")


def help_me(request):
    my_dict = {'help_insert': 'Now I am coming from appTwo/help_me.html'}
    return render(request, 'appTwo/help_me.html', context=my_dict)
