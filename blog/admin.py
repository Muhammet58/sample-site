from django.contrib import admin
from . models import Main_model

class Main_admin(admin.ModelAdmin):
    list_display = ('title', 'slug',)
    readonly_fields = ('slug',)

admin.site.register(Main_model, Main_admin)