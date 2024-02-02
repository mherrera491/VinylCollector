from django.shortcuts import render
from django.http import HttpResponse
from.models import Vinyl
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# class Vinyl:
#     def __init__(self, album, artist, release_year, genre, album_cover):
#         self.album = album
#         self.artist = artist
#         self.release_year = release_year
#         self.genre = genre
#         self.album_cover = album_cover

# vinyls = [
#     Vinyl('Swimming', 'Mac Miller', '2018', 'Hip-Hop/Rap', 'https://upload.wikimedia.org/wikipedia/en/5/5e/Mac_Miller_-_Swimming.png'),
#     Vinyl('Thee Sacred Souls', 'Thee Sacred Souls', '2022', 'R&B/Soul', 'https://i.scdn.co/image/ab67616d00001e024bc05e5b1e506a6acea17148'),
#     Vinyl('Ctrl', 'SZA', '2017', 'R&B', 'https://upload.wikimedia.org/wikipedia/en/b/bf/SZA_-_Ctrl_cover.png'),
# ]

def vinyl_index(request):
    vinyls = Vinyl.objects.all()
    return render(request, 'vinyl/index.html', { 'vinyls': vinyls })
        
def vinyl_detail(request, vinyl_id):
    vinyl = Vinyl.objects.get(id=vinyl_id)
    return render(request, 'vinyl/detail.html', { 'vinyl': vinyl })