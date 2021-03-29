from django.conf import settings
from django.conf.urls import url
from django.urls import path
from django.views.generic import RedirectView
from appTwo import views


urlpatterns = [
    url(r'^$', views.help_me, name='help'),
    url(r'^favicon\.ico$', RedirectView.as_view(url=settings.STATIC_URL + 'images/favicon.ico')),
    path('', views.index, name='Index'),
    path('users', views.users, name='User List'),
]
