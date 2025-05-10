from django.contrib import admin
from django.utils.html import format_html

from cars.models import Car


# Register your models here.
class CarAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html(f'<img src="{object.car_photo.url}" width="100" />')

    thumbnail.short_description = 'Photo'
    list_display = ('car_title', 'thumbnail', 'model', 'color', 'condition', 'price', 'is_featured')
    list_editable = ('price', 'is_featured')
    list_display_links = ('car_title', 'thumbnail', 'model', 'color', 'condition')
    search_fields = ('id', 'car_title', 'color', 'model', 'condition')
    list_filter = ('model', 'fuel_type', 'city')


admin.site.register(Car, CarAdmin)
