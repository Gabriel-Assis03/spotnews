from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .models import News


def index(request):
    context = {'news': News.objects.all()}
    return render(request, 'home.html', context)


def news_details(request, id):
    try:
        new = get_object_or_404(News, id=id)
        return render(request, 'news_details.html', {'new': new})
    except Http404:
        return render(request, '404.html')
    # context = {'new': News.objects.first(id)}
    # return render(request, 'news_details.html', context)
