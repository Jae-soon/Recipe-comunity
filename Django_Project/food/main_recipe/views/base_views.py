from django.shortcuts import render, get_object_or_404
from ..models import main_recipe, Photo


def index(request):
    return render(request, 'main/main.html')


def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(main_recipe, pk = recipe_id)
    context = {'recipe' : recipe}
    return render(request, 'main/recipe_detail.html', context)