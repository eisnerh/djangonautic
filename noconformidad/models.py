from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from django.db.models import Manager


class Area(models.Model):
    area_name = models.CharField(max_length=100)

    def __str__(self):
        return self.area_name


class Material(models.Model):
    material_number = models.IntegerField(default='1')
    short_description = models.TextField(default='')
    material_cost = models.FloatField(default='0')

    def __str__(self):
        return self.short_description


class Cause(models.Model):
    cause_name = models.CharField(max_length=100)

    def __str__(self):
        return self.cause_name


class Description(models.Model):
    description_name = models.CharField(max_length=100)

    def __str__(self):
        return self.description_name


class NotCompliant(models.Model):
    author = models.ForeignKey(User, default=None, on_delete='CASCADE')
    email_to = models.CharField(max_length=100, default='')
    area = models.ManyToManyField(Area)
    material_code: Manager = models.ManyToManyField(Material)
    material_quantity = models.IntegerField
    cause_select = models.ManyToManyField(Cause)
    description_select = models.ManyToManyField(Description)
    thumb_lot = models.ImageField(default='default.png', blank=True)
    thumb_damage = models.ImageField(default='default.png', blank=True)
    thumb_total = models.ImageField(default='default.png', blank=True)

    def __str__(self):
        return self.material_code
