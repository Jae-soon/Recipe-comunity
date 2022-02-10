from django.contrib import admin
from .models import share_recipe

class share_recipeAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(share_recipe, share_recipeAdmin)