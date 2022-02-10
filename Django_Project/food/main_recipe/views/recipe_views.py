from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from ..models import main_recipe, Photo
from ..forms import RecipeForm


@login_required(login_url = "common:login")
def recipe_create(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.create_date = timezone.now()
            recipe.save()
            for img in request.FILES.getlist('imgs'):
                photo = Photo()
                photo.recipe = recipe
                photo.image = img
                photo.save()

            if recipe.menu == "한식":
                return redirect('main:korean')
            elif recipe.menu == "중식":
                return redirect('main:chinese')
            elif recipe.menu == "일식":
                return redirect('main:japanese')
            else:
                return redirect('main:western')
    else:
        form = RecipeForm()
    context = {'form' : form}
    return render(request, 'main/recipe_form.html', context)


@login_required(login_url = "common:login")
def recipe_modify(request, recipe_id):
    recipe = get_object_or_404(main_recipe, pk=recipe_id)
    if request.user != recipe.author:
        messages.error(request, '수정 권한이 없습니다')
        return redirect('main:recipe_detail', recipe_id = recipe.id)

    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.modify_date = timezone.now()
            recipe.save()
            for img in request.FILES.getlist('imgs'):
                photo = Photo()
                photo.recipe = recipe
                photo.image = img
                photo.save()
            return redirect('main:recipe_detail', recipe_id = recipe.id)
    else:
        form = RecipeForm(instance=recipe)
    context = {'form': form}
    return render(request, 'main/recipe_form.html', context)


@login_required(login_url = "common:login")
def recipe_delete(request, recipe_id):
    recipe = get_object_or_404(main_recipe, pk=recipe_id)
    if request.user != recipe.author:
        messages.error(request, '삭제 권한이 없습니다')
        return redirect('main:recipe_detail', recipe_id = recipe.id)
    recipe.delete()
    return redirect('main:index')