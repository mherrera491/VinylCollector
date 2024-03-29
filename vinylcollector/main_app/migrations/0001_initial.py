# Generated by Django 5.0.1 on 2024-02-02 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vinyl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album', models.CharField(max_length=100)),
                ('artist', models.CharField(max_length=100)),
                ('release_year', models.IntegerField()),
                ('genre', models.CharField(max_length=100)),
                ('album_cover', models.URLField()),
            ],
        ),
    ]
