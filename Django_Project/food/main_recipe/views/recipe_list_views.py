from django.core.paginator import Paginator
from django.shortcuts import render
from ..models import main_recipe


def korean(request):
    page = request.GET.get('page', '1')
    korean_main_recipe = main_recipe.objects.filter(menu__contains='한식')
    paginator = Paginator(korean_main_recipe, 5)
    page_obj = paginator.get_page(page)
    context = {'recipe_list': page_obj}
    return render(request, 'main/korean_recipe_list.html', context)


def chinese(request):
    page = request.GET.get('page', '1')
    chinese_main_recipe = main_recipe.objects.filter(menu__contains='중식')
    paginator = Paginator(chinese_main_recipe, 5)
    page_obj = paginator.get_page(page)
    context = {'recipe_list': page_obj}
    return render(request, 'main/chinese_recipe_list.html', context)


def western(request):
    page = request.GET.get('page', '1')
    western_main_recipe = main_recipe.objects.filter(menu__contains='양식')
    paginator = Paginator(western_main_recipe, 5)
    page_obj = paginator.get_page(page)
    context = {'recipe_list': page_obj}
    return render(request, 'main/western_recipe_list.html', context)


def japanese(request):
    page = request.GET.get('page', '1')
    japanese_main_recipe = main_recipe.objects.filter(menu__contains='일식')
    paginator = Paginator(japanese_main_recipe, 5)
    page_obj = paginator.get_page(page)
    context = {'recipe_list': page_obj}
    return render(request, 'main/japanese_recipe_list.html', context)