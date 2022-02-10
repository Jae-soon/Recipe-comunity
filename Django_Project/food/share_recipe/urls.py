from django.urls import path
from .views import answer_views, base_views, comment_views, recipe_list_views, recipe_views, voter_views

app_name = 'share'

urlpatterns = [
    path('', base_views.index, name = 'index'),
    path('korean/', recipe_list_views.korean, name = 'korean'),
    path('chinese/', recipe_list_views.chinese, name = 'chinese'),
    path('western/', recipe_list_views.western, name = 'western'),
    path('japanese/', recipe_list_views.japanese, name = 'japanese'),
    path('<int:recipe_id>/', base_views.recipe_detail, name = 'recipe_detail'),
    path('answer/create/<int:recipe_id>/', answer_views.answer_create, name = 'answer_create'),
    path('recipe/create/', recipe_views.recipe_create, name = 'recipe_create'),
    path('recipe/modify/<int:recipe_id>/', recipe_views.recipe_modify, name = 'recipe_modify'),
    path('recipe/delete/<int:recipe_id>/', recipe_views.recipe_delete, name = 'recipe_delete'),
    path('answer/modify/<int:answer_id>/', answer_views.answer_modify, name = 'answer_modify'),
    path('answer/delete/<int:answer_id>/', answer_views.answer_delete, name = 'answer_delete'),
    path('comment/create/recipe/<int:recipe_id>/', comment_views.comment_create_recipe, name = 'comment_create_recipe'),
    path('comment/modify/recipe/<int:comment_id>/', comment_views.comment_modify_recipe, name = 'comment_modify_recipe'),
    path('comment/delete/recipe/<int:comment_id>/', comment_views.comment_delete_recipe, name = 'comment_delete_recipe'),
    path('comment/create/answer/<int:answer_id>/', comment_views.comment_create_answer, name='comment_create_answer'),
    path('comment/modify/answer/<int:comment_id>/', comment_views.comment_modify_answer, name='comment_modify_answer'),
    path('comment/delete/answer/<int:comment_id>/', comment_views.comment_delete_answer, name='comment_delete_answer'),
    path('vote/question/<int:recipe_id>/', voter_views.vote_recipe, name='vote_recipe'),
    path('vote/answer/<int:answer_id>/', voter_views.vote_answer, name='vote_answer'),
]