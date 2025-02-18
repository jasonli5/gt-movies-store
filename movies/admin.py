from django.contrib import admin
from django.utils.html import format_html

from .models import Movie, Review

class MovieAdmin(admin.ModelAdmin):
    ordering = ['name']
    search_fields = ['name']
    readonly_fields = ("movie_poster",)

    def movie_poster(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="300" height="400" style="object-fit:cover; border-radius:10px;" />',
                obj.image.url)
        return "No Image Available"


admin.site.register(Movie, MovieAdmin)
admin.site.register(Review)