from django.contrib import admin

from .models import Customer, Movie

# Register your models here.

admin.site.register([Customer, Movie])
