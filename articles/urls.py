from django.urls import path
from . import views
from django.urls import path

from . import views

app_name = 'articles'


urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('<str:slug>', views.article_details, name='details'),
]
