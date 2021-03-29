from django.contrib import admin
from first_app.models import AccessRecord, Topic, Webpage

admin.site.register([AccessRecord, Topic, Webpage])
