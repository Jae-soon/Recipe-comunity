from django.core.paginator import Paginator
from django.shortcuts import render
from ..models import share_recipe
from django.db.models import Q, Count


def best_recipe_list(request):
    best_recipe_li = []
    page = request.GET.get('page', '1')
    best_recipe = share_recipe.objects.annotate(num_voter=Count('voter')).filter(num_voter__gt=0)
    paginator = Paginator(best_recipe, 5)
    page_obj = paginator.get_page(page)
    context = {'recipe_list': page_obj}
    return render(request, 'best/best_recipe_list.html', context)


def korean(request):
    page = request.GET.get('page', '1')
    kw = request.GET.get('kw', '')
    so = request.GET.get('so', 'recent')  # 정렬기준

    # 정렬
    if so == 'recommend':
        korean_share_recipe = share_recipe.objects.annotate(num_voter=Count('voter')).filter(menu__contains='한식').order_by('-num_voter', '-create_date')
    elif so == 'popular':
        korean_share_recipe = share_recipe.objects.annotate(num_answer=Count('answer')).filter(menu__contains='한식').order_by('-num_answer', '-create_date')
    else:  # recent
        korean_share_recipe = share_recipe.objects.filter(menu__contains='한식')
    # korean_share_recipe = share_recipe.objects.filter(menu__contains='한식')
    if kw:
        korean_share_recipe = korean_share_recipe.filter(
            Q(subject__icontains=kw) |  # 제목검색
            Q(material__icontains=kw) |  # 재료검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이검색
            Q(answer__author__username__icontains=kw)  # 답변 글쓴이검색
        ).distinct()
    paginator = Paginator(korean_share_recipe, 5)
    page_obj = paginator.get_page(page)
    context = {'recipe_list': page_obj, 'page': page, 'kw': kw, 'so' : so}
    return render(request, 'share/korean_recipe_list.html', context)

def chinese(request):
    page = request.GET.get('page', '1')
    kw = request.GET.get('kw', '')
    so = request.GET.get('so', 'recent')  # 정렬기준

    # 정렬
    if so == 'recommend':
        chinese_share_recipe = share_recipe.objects.annotate(num_voter=Count('voter')).filter(
            menu__contains='중식').order_by('-num_voter', '-create_date')
    elif so == 'popular':
        chinese_share_recipe = share_recipe.objects.annotate(num_answer=Count('answer')).filter(
            menu__contains='중식').order_by('-num_answer', '-create_date')
    else:  # recent
        chinese_share_recipe = share_recipe.objects.filter(menu__contains='중식')
    if kw:
        chinese_share_recipe = chinese_share_recipe.filter(
            Q(subject__icontains=kw) |  # 제목검색
            Q(material__icontains=kw) |  # 재료검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이검색
            Q(answer__author__username__icontains=kw)  # 답변 글쓴이검색
        ).distinct()
    paginator = Paginator(chinese_share_recipe, 5)
    page_obj = paginator.get_page(page)
    context = {'recipe_list': page_obj, 'page': page, 'kw': kw, 'so': so}
    return render(request, 'share/chinese_recipe_list.html', context)

def western(request):
    page = request.GET.get('page', '1')
    kw = request.GET.get('kw', '')
    so = request.GET.get('so', 'recent')  # 정렬기준

    # 정렬
    if so == 'recommend':
        western_share_recipe = share_recipe.objects.annotate(num_voter=Count('voter')).filter(
            menu__contains='양식').order_by('-num_voter', '-create_date')
    elif so == 'popular':
        western_share_recipe = share_recipe.objects.annotate(num_answer=Count('answer')).filter(
            menu__contains='양식').order_by('-num_answer', '-create_date')
    else:  # recent
        western_share_recipe = share_recipe.objects.filter(menu__contains='양식')
    if kw:
        western_share_recipe = western_share_recipe.filter(
            Q(subject__icontains=kw) |  # 제목검색
            Q(material__icontains=kw) |  # 재료검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이검색
            Q(answer__author__username__icontains=kw)  # 답변 글쓴이검색
        ).distinct()
    paginator = Paginator(western_share_recipe, 5)
    page_obj = paginator.get_page(page)
    context = {'recipe_list': page_obj, 'page': page, 'kw': kw, 'so': so}
    return render(request, 'share/western_recipe_list.html', context)


def japanese(request):
    page = request.GET.get('page', '1')
    kw = request.GET.get('kw', '')
    so = request.GET.get('so', 'recent')  # 정렬기준

    # 정렬
    if so == 'recommend':
        japanese_share_recipe = share_recipe.objects.annotate(num_voter=Count('voter')).filter(
            menu__contains='일식').order_by('-num_voter', '-create_date')
    elif so == 'popular':
        japanese_share_recipe = share_recipe.objects.annotate(num_answer=Count('answer')).filter(
            menu__contains='일식').order_by('-num_answer', '-create_date')
    else:  # recent
        japanese_share_recipe = share_recipe.objects.filter(menu__contains='일식')
    if kw:
        japanese_share_recipe = japanese_share_recipe.filter(
            Q(subject__icontains=kw) |  # 제목검색
            Q(material__icontains=kw) |  # 재료검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이검색
            Q(answer__author__username__icontains=kw)  # 답변 글쓴이검색
        ).distinct()
    paginator = Paginator(japanese_share_recipe, 5)
    page_obj = paginator.get_page(page)
    context = {'recipe_list': page_obj, 'page': page, 'kw': kw, 'so': so}
    return render(request, 'share/japanese_recipe_list.html', context)