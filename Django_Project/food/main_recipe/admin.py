from django.contrib import admin
from .models import main_recipe, Photo


class main_recipeAdmin(admin.ModelAdmin):
    search_fields = ['subject']


class PhotoInline(admin.TabularInline):
    model = Photo


class PostAdmin(admin.ModelAdmin):
    inlines = [PhotoInline, ]



admin.site.register(main_recipe, PostAdmin)