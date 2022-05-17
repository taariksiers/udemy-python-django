from django.conf import settings
from django.contrib.auth import views as auth_views
from django.urls import path, re_path
from django.views.generic import RedirectView

from accounts import views

app_name = "accounts"

urlpatterns = [
    # url(r'^favicon\.ico$', RedirectView.as_view(url=settings.STATIC_URL + 'images/favicon.ico')),
    path('favicon.ico', RedirectView.as_view(url=settings.STATIC_URL + 'images/favicon.ico')),
    re_path("login/$", auth_views.LoginView.as_view(template_name="accounts/login.html"), name="login"),
    re_path("logout/$", auth_views.LogoutView.as_view(), name="logout"),
    path("signup", views.SignUp.as_view(), name="signup"),
]
