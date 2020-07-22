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
   artists =  ", ".join(artist['name'] for artist in album['artists'])

   message = f"Le nom de l'album est {album['name']}. Il a été écrit par {artists}"
   return HttpResponse(message)

def search(request):
   query = request.GET.get('query')
   if not query :
      message = "Aucun artiste demandé"
   else:
      albums = [
         album for album in ALBUMS
         if query in [artist['name'] for artist in album['artists']]
      ]
      print ("albums avant le formatage: ", albums)
      if len(albums) == 0:
         message = "Pas d'album pour cet artiste"
      else:
         albums = ["<li>{}</li>".format(album['name']) for album in albums]
         print("albums après le formatage dans <li>:", albums)
         message= """
            Voici les albums correspondant à la requête:
            <ul>
               {}
            </ul>
            
         """.format("\n".join(albums))

   return HttpResponse(message)