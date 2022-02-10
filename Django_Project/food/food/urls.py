from django.contrib import admin
from django.urls import path
from share_recipe.views import recipe_list_views

app_name = 'best'

urlpatterns = [
    path('', recipe_list_views.best_recipe_list, name = 'index'),
]