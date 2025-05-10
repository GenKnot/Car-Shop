from django.contrib import admin
from .models import Contact


# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'car_title', 'city')
    list_display_links = ('id', 'email', 'car_title', 'city')
    search_fields = ('id', 'email', 'car_title', 'city', 'first_name', 'last_name')
    list_per_page = 30
    list_filter = ('car_title', 'city')


admin.site.register(Contact, ContactAdmin)
