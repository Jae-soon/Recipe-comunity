from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.utils import timezone
from ..forms import AnswerForm
from ..models import share_recipe, Answer


@login_required(login_url = "common:login")
def answer_create(request, recipe_id):
    recipe = get_object_or_404(share_recipe, pk = recipe_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.create_date = timezone.now()
            answer.recipe = recipe
            answer.save()
            return redirect('{}#answer_{}'.format(
                resolve_url('share:recipe_detail', recipe_id = recipe.id), answer.id))
    else:
        form = AnswerForm()
    context = {'recipe' : recipe, 'form' : form}
    return render(request, 'share/recipe_detail.html', context)


@login_required(login_url = "common:login")
def answer_modify(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '수정 권한이 없습니다')
        return redirect('share:recipe_detail', recipe_id = answer.recipe.id)

    if request.method == 'POST':
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.modify_date = timezone.now()
            answer.save()
            return redirect('{}#answer_{}'.format(
                resolve_url('share:recipe_detail', recipe_id = answer.recipe.id), answer.id))
    else:
        form = AnswerForm(instance=answer)
    context = {'answer' : answer, 'form': form}
    return render(request, 'share/answer_form.html', context)


@login_required(login_url = "common:login")
def answer_delete(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '삭제 권한이 없습니다')
    else:
        answer.delete()
    return redirect('share:recipe_detail', recipe_id = answer.recipe.id)