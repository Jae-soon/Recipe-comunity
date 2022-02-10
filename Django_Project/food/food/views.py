from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import RecipeForm, AnswerForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


def mainpage(request):
    return render(request, 'mainpage/mainpage.html')


