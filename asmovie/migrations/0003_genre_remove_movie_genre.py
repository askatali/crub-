# Generated by Django 5.0 on 2024-01-23 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asmovie', '0002_movie_movie_age_movie_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
            },
        ),
        migrations.RemoveField(
            model_name='movie',
            name='genre',
        ),
    ]
