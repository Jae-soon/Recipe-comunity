from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from ..models import share_recipe, Answer


@login_required(login_url='common:login')
def vote_recipe(request, recipe_id):
    recipe = get_object_or_404(share_recipe, pk = recipe_id)
    if request.user == recipe.author:
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        recipe.voter.add(request.user)
    return redirect('share:recipe_detail', recipe_id = recipe.id)


@login_required(login_url='common:login')
def vote_answer(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user == answer.author:
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        answer.voter.add(request.user)
    return redirect('share:recipe_detail', recipe_id =answer.recipe.id)