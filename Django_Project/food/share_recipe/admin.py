from django.contrib import admin
from .models import share_recipe, Photo

class share_recipeAdmin(admin.ModelAdmin):
    search_fields = ['subject']


class PhotoInline(admin.TabularInline):
    model = Photo


class PostAdmin(admin.ModelAdmin):
    inlines = [PhotoInline, ]



admin.site.register(share_recipe, PostAdmin)