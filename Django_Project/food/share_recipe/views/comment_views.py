from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.utils import timezone
from ..forms import CommentForm
from ..models import share_recipe, Answer, Comment

@login_required(login_url = "common:login")
def comment_create_recipe(request, recipe_id):
    recipe = get_object_or_404(share_recipe, pk = recipe_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.author = request.user
            comment.create_date = timezone.now()
            comment.recipe = recipe
            comment.save()
            return redirect('{}#comment_{}'.format(
                resolve_url('share:recipe_detail', recipe_id = comment.recipe.id), comment.id))
    else:
        form = CommentForm()
    context = {'form' : form}
    return render(request, 'share/comment_form.html', context)


@login_required(login_url='common:login')
def comment_modify_recipe(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '댓글수정권한이 없습니다')
        return redirect('share:recipe_detail', recipe_id=comment.recipe.id)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.modify_date = timezone.now()
            comment.save()
            return redirect('{}#comment_{}'.format(
                resolve_url('share:recipe_detail', recipe_id=comment.recipe.id), comment.id))
    else:
        form = CommentForm(instance=comment)
    context = {'form': form}
    return render(request, 'share/comment_form.html', context)


@login_required(login_url='common:login')
def comment_delete_recipe(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '댓글삭제권한이 없습니다')
        return redirect('share:recipe_detail', recipe_id=comment.recipe.id)
    else:
        comment.delete()
    return redirect('share:recipe_detail', recipe_id=comment.recipe.id)


@login_required(login_url='common:login')
def comment_create_answer(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.create_date = timezone.now()
            comment.answer = answer
            comment.save()
            return redirect('{}#comment_{}'.format(
                resolve_url('share:recipe_detail', recipe_id=comment.answer.recipe.id), comment.id))
    else:
        form = CommentForm()
    context = {'form': form}
    return render(request, 'share/comment_form.html', context)


@login_required(login_url='common:login')
def comment_modify_answer(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '댓글수정권한이 없습니다')
        return redirect('share:recipe_detail', recipe_id=comment.answer.recipe.id)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.modify_date = timezone.now()
            comment.save()
            return redirect('{}#comment_{}'.format(
                resolve_url('share:recipe_detail', recipe_id=comment.recipe.id), comment.id))
    else:
        form = CommentForm(instance=comment)
    context = {'form': form}
    return render(request, 'share/comment_form.html', context)


@login_required(login_url='common:login')
def comment_delete_answer(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '댓글삭제권한이 없습니다')
        return redirect('share:recipe_detail', recipe_id=comment.answer.recipe.id)
    else:
        comment.delete()
    return redirect('share:recipe_detail', recipe_id=comment.answer.recipe.id)