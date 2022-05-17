"""ProTwo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import RedirectView
from appTwo import views, urls

urlpatterns = [
    re_path(r'^favicon\.ico$', RedirectView.as_view(url=settings.STATIC_URL + 'images/favicon.ico')),
    re_path(r'^index/$|^$', views.index, name='Index'),
    path('users/', include(urls)),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
                      re_path(r'^__debug__/', include(debug_toolbar.urls))
                  ] + urlpatterns
