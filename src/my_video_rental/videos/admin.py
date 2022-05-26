from django.contrib import admin

from .models import Customer, Movie

# non overriden models
admin.site.register([Customer])

class MovieAdmin(admin.ModelAdmin):

    fields = ["release_year", "title", "length"]

    search_fields = ["title", "length"]

    list_filter = ["release_year", "length"]

    list_display = ["title", "release_year", "length"]

    list_editable = ["length"]


# tuplised instead of list to avoid _meta error - package override with based on model
admin.site.register(Movie, MovieAdmin)
