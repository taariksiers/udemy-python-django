from django.contrib import admin
from blog.models import Comment, Post

admin.site.register([Comment, Post])
