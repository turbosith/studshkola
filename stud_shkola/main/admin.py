from django.contrib import admin

# Register your models here.
from .forms import AddQuestionForm
from .models import *


class UniversitiesAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'photo')
    list_display_links = ('id','name')
    prepopulated_fields = ({"slug":("name",)})


class MainAdmin(admin.ModelAdmin):
    list_display = ('id','question','cat', 'photo', 'time_create','is_published')
    list_display_links = ('id','question')
    search_fields = ('question', 'cat')
    list_editable = ('is_published',)
    list_filter=('is_published','time_create')
    '''
class MainAd(admin.ModelAdmin):
    list_display = ('id','question','cat', 'photo', 'time_create','is_published')
    list_display_links = ('id','question')
    search_fields = ('question', 'cat')
    list_editable = ('is_published',)
    list_filter=('is_published','time_create')
    form = AddQuestionForm
    '''
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id','name')
    search_fields = ('name',)
    prepopulated_fields = ({"slug": ("name",)})

class LevelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'text','author', 'time_create')
    list_display_links = ('id', 'text')
    search_fields = ('text',)
admin.site.register(Comments,CommentAdmin)
admin.site.register(LevelEducation, LevelAdmin)
admin.site.register(Universities, UniversitiesAdmin)
admin.site.register(Questions,MainAdmin )
admin.site.register(Category, CategoryAdmin)
