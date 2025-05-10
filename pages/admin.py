from django.contrib import admin
from pages.models import Team
from django.utils.html import format_html

# Register your models here.
admin.site.site_header = 'Car Site'
admin.site.site_title = 'Car Site'
admin.site.index_title = "Car Site Panel"


class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html(f'<img src="{object.photo.url}" width="80" />')

    thumbnail.short_description = 'Photo'
    list_display = ('id', 'thumbnail', 'first_name', 'last_name', 'designation', 'create_data')
    list_display_links = ('id', 'first_name', 'last_name')
    search_fields = ('first_name', 'last_name', 'designation')
    list_filter = ('designation',)


admin.site.register(Team, TeamAdmin)
