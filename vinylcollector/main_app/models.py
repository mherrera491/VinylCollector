from django.db import models
from django.urls import reverse

# Create your models here.
class Vinyl(models.Model):
    album = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    release_year = models.IntegerField()
    genre = models.CharField(max_length=100)
    album_cover = models.URLField()

    def __str__(self):
        return self.album
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'vinyl_id': self.id})
    
class Purchased(models.Model):
    date = models.DateField('Purchased Date')
    
    vinyl = models.ForeignKey(Vinyl, on_delete=models.CASCADE)

    def __str__(self):
        return f"Purchased on {self.date}"
    
    class Meta:
        ordering = ['-date']
        verbose_name_plural = "Purchased"