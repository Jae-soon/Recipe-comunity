from django.shortcuts import render, get_object_or_404
from ..models import share_recipe


def index(request):
    return render(request, 'share/main.html')


def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(share_recipe, pk = recipe_id)
    context = {'recipe' : recipe}
    return render(request, 'share/recipe_detail.html', context)