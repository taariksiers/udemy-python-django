from django.contrib import admin
from basic_app.models import School, Student

admin.site.register([School, Student])
