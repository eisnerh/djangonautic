from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models import Manager


class Area(models.Model):
    area_name = models.CharField(max_length=100, default='')

    def __str__(self):
        if self.area_name is None:
            return "ERROR- Area NAME IS NULL"
        return self.area_name


class Material(models.Model):
    material_number = models.IntegerField(default='1')
    short_description = models.TextField(default='')
    material_cost = models.FloatField(default='0')

    def __str__(self):
        if self.short_description is None:
            return "ERROR- Short Description IS NULL"
        return self.short_description


class Cause(models.Model):
    cause_name = models.CharField(max_length=100, default='')

    def __str__(self):
        if self.cause_name is None:
            return "ERROR- Cause NAME IS NULL"
        return self.cause_name


class Description(models.Model):
    description_name = models.CharField(max_length=100)

    def __str__(self):
        if self.description_name is None:
            return "ERROR- Description NAME IS NULL"
        return self.description_name


class NotCompliant(models.Model):
    author = models.ForeignKey(User, default=None, on_delete='CASCADE')
    email_to = models.CharField(max_length=100, default='')
    area = models.ManyToManyField(Area, default='CD04')
    material_code: Manager = models.ManyToManyField(Material, default='')
    material_quantity = models.IntegerField(default=1)
    cause_select = models.ManyToManyField(Cause)
    description_select = models.ManyToManyField(Description)
    thumb_lot = models.ImageField(default='default.png', blank=True)
    thumb_damage = models.ImageField(default='default.png', blank=True)
    thumb_total = models.ImageField(default='default.png', blank=True)

    def __str__(self):
        return self.email_to


class NoConforme(models.Model):
    author = models.CharField(max_length=100, default='')
    email_to = models.CharField(max_length=100, default='')
    area = models.CharField(max_length=100, default='CD04')
    material_code = models.IntegerField(help_text='Digita el Código del Material', default='1')
    material_quantity = models.IntegerField(default=1)
    cause_select = models.CharField(max_length=100, default='')
    thumb_lot = models.ImageField(default='default.png', blank=True)
    thumb_damage = models.ImageField(default='default.png', blank=True)
    thumb_total = models.ImageField(default='default.png', blank=True)
