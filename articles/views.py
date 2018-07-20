from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .import forms
from .models import Article


# Create your assets here.


def article_list(request):
    articles = Article.objects.all().order_by("date")

    return render(request, "articles/articles_list.html", {'articles': articles})


def article_details(request, slug):
    article = Article.objects.get(slug=slug)

    articles = get_object_or_404(Article, slug=slug)
    return render(request, "articles/article_details.html", {'article': article, 'articles': articles})


@login_required(login_url='/accounts/login/')
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            # save article to db
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('articles:article_list')
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/article_create.html', {'form': form})
