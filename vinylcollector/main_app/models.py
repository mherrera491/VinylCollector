from django.db import models

# Create your models here.
class Vinyl(models.Model):
    album = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    release_year = models.IntegerField()
    genre = models.CharField(max_length=100)
    album_cover = models.URLField()

    def __str__(self):
        return self.album