# Generated by Django 2.0.7 on 2018-07-22 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noconformidad', '0003_auto_20180721_1301'),
    ]

    operations = [
        migrations.AddField(
            model_name='notcompliant',
            name='material_quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='notcompliant',
            name='area',
            field=models.ManyToManyField(default='CD04', to='noconformidad.Area'),
        ),
        migrations.AlterField(
            model_name='notcompliant',
            name='material_code',
            field=models.ManyToManyField(default='', to='noconformidad.Material'),
        ),
    ]
