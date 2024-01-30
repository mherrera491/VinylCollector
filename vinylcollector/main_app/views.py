from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

class Vinyl:
    def __init__(self, album, artist, release_year, genre):
        self.album = album
        self.artist = artist
        self.release_year = release_year
        self.genre = genre

vinyls = [
    Vinyl('Swimming', 'Mac Miller', '2018', 'Hip-Hop/Rap'),
    Vinyl('Thee Sacred Souls', 'Thee Sacred Souls', '2022', 'R&B/Soul'),
    Vinyl('Ctrl', 'SZA', '2017', 'R&B'),
]

def vinyl_index(request):
    return render(request, 'vinyl/index.html', { 'vinyls': vinyls })
        