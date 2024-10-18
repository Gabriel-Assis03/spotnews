from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .models import News, Category
from .forms import CategoryModelsForm, NewsModelsForm


def index(request):
    context = {'news': News.objects.all()}
    return render(request, 'home.html', context)


def news_details(request, id):
    try:
        new = get_object_or_404(News, id=id)
        return render(request, 'news_details.html', {'new': new})
    except Http404:
        return render(request, '404.html')


def categories_form(request):
    if request.method == "POST":
        form = CategoryModelsForm(request.POST)
        if form.is_valid():
            Category.objects.create(**form.cleaned_data)
            return redirect("home-page")
    context = {'form': CategoryModelsForm()}
    return render(request, 'categories_form.html', context)


def news_form(request):
    if request.method == "POST":
        form = NewsModelsForm(request.POST, request.FILES)
        if form.is_valid():
            news = News.objects.create(
                title=form.cleaned_data.get('title'),
                content=form.cleaned_data.get('content'),
                author=form.cleaned_data.get('author'),
                created_at=form.cleaned_data.get('created_at'),
                image=form.cleaned_data.get('image'),
            )
            news.categories.set(form.cleaned_data.get('categories'))
            news.save()
            return redirect("home-page")
    context = {'form': NewsModelsForm()}
    return render(request, 'news_form.html', context)
