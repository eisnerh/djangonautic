from django.shortcuts import render, get_object_or_404

from .models import Article


# Create your assets here.


def article_list(request):
    articles = Article.objects.all().order_by("date")

    return render(request, "articles/articles_list.html", {'articles': articles})


def article_details(request, slug):
    article = Article.objects.get(slug=slug)

    articles = get_object_or_404(Article, slug=slug)
    return render(request, "articles/article_details.html", {'article': article, 'articles': articles})
