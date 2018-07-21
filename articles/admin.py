# Register your models here.
from django.contrib import admin

from articles.models import Article
from noconformidad.models import NotCompliant

admin.site.register(Article)
