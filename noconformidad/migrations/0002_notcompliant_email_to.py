# Generated by Django 2.0.7 on 2018-07-21 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noconformidad', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notcompliant',
            name='email_to',
            field=models.CharField(default='', max_length=100),
        ),
    ]
