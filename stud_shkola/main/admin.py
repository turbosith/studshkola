from django.contrib import admin

# Register your models here.
from .models import *



class MainAdmin(admin.ModelAdmin):
    list_display = ('id','question','cat', 'photo', 'time_create','is_published')
    list_display_links = ('id','question')
    search_fields = ('question', 'cat')
    list_editable = ('is_published',)
    list_filter=('is_published','time_create')
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id','name')
    search_fields = ('name',)
admin.site.register(questions,MainAdmin )
admin.site.register(Category, CategoryAdmin)