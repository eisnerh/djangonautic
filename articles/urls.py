from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('details/<int:pk>', views.article_details, name='details'),
]
