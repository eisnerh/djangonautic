# Generated by Django 2.0.7 on 2018-07-22 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noconformidad', '0007_auto_20180721_2208'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noconforme',
            name='material_code',
        ),
        migrations.AddField(
            model_name='noconforme',
            name='material_code',
            field=models.IntegerField(default='1', help_text='Digita el Código del Material'),
        ),
    ]
