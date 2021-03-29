from django.contrib import admin
from first_app.models import AccessRecord, User, Topic, Webpage

admin.site.register([AccessRecord, User, Topic, Webpage])
