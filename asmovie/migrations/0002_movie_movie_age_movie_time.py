# Generated by Django 5.0 on 2024-01-23 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asmovie', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='movie_age',
            field=models.IntegerField(default=18),
        ),
        migrations.AddField(
            model_name='movie',
            name='time',
            field=models.IntegerField(default=58),
        ),
    ]
