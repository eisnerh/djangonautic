"""djangonautic URL Configuration

The `urlpatterns` list routes URLs to assets. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function assets
    1. Add an import:  from my_app import assets
    2. Add a URL to urlpatterns:  path('', assets.home, name='home')
Class-based assets
    1. Add an import:  from other_app.assets import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include

import articles
from articles import views
from .views import about, homepage
from articles import views as articles_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.article_create, name='create'),
    path('homepage/', homepage, name='homepage'),
    path('about', about, name='about'),
    path('articles/', include('articles.urls')),
    path('accounts/', include('accounts.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
