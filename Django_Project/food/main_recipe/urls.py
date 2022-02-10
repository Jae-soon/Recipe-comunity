from django.contrib import admin
from django.urls import path
from .views import base_views, recipe_list_views, recipe_views


app_name = 'main'

urlpatterns = [
    path('', base_views.index, name = 'index'),
    path('korean/', recipe_list_views.korean, name = 'korean'),
    path('chinese/', recipe_list_views.chinese, name = 'chinese'),
    path('western/', recipe_list_views.western, name = 'western'),
    path('japanese/', recipe_list_views.japanese, name = 'japanese'),
    path('<int:recipe_id>/', base_views.recipe_detail, name = 'recipe_detail'),
    path('recipe/create/', recipe_views.recipe_create, name='recipe_create'),
    path('recipe/modify/<int:recipe_id>/', recipe_views.recipe_modify, name = 'recipe_modify'),
    path('recipe/delete/<int:recipe_id>/', recipe_views.recipe_delete, name = 'recipe_delete'),
]