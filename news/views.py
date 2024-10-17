from django.shortcuts import render, redirect
from .models import News


def index(request):
    context = {'news': News.objects.all()}
    return render(request, 'home.html', context)
