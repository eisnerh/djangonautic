from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=False)
    thumb = models.ImageField(default='default.png', blank=True)
    author = models.ForeignKey(User, default=None, on_delete='CASCADE')

    def __str__(self):
        return self.title

    @property
    def snippet(self):
        return self.body[0:50] + '...'
