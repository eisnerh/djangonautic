# Generated by Django 2.0.7 on 2018-07-22 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noconformidad', '0005_auto_20180721_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noconforme',
            name='cause_select',
            field=models.ManyToManyField(default='', to='noconformidad.Cause'),
        ),
    ]
