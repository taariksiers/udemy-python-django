from django.conf import settings
from django.urls import path, re_path
from django.views.generic import RedirectView
from appTwo import views


urlpatterns = [
    re_path(r'^favicon\.ico$', RedirectView.as_view(url=settings.STATIC_URL + 'images/favicon.ico')),
    path('', views.index, name='Index'),
    path('users', views.users, name='User List'),
]
