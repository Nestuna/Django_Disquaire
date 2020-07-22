from django.shortcuts import render
from django.http import HttpResponse

from .models import ALBUMS

# Create your views here.
def index(request):
   message = "Salut tout le monde !"
   return HttpResponse(message)

def listing(request):
   albums = ["<li>{}</li>".format(album['name']) for album in ALBUMS]
   message = """<ul>{}</ul>""".format("\n".join(albums))
   
   return HttpResponse(message)

def details(request, album_id):
   id = int(album_id)
   album = ALBUMS[id]
   artists =  album['artists']['name']

   message = f"Le nom de l'album est {album['name']}. Il a été écrit par {artists}"
   return HttpResponse(message)

