from django.shortcuts import render

from .models import Article


# Create your assets here.


def article_list(request):
    articles = Article.objects.all().order_by("date")

    return render(request, "articles/articles_list.html", {'articles': articles})


def article_details(request, pk):
    details = Article.objects.get(id=pk)
    return render(request, "articles/details.html", {'details': details})
