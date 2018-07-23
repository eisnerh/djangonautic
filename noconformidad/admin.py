from django.contrib import admin
from .models import NotCompliant, Description, Cause, Material, Area, NoConforme

# Register your models here.
admin.site.register(NotCompliant)
admin.site.register(Description)
admin.site.register(Cause)
admin.site.register(Material)
admin.site.register(Area)
admin.site.register(NoConforme)
