from django.shortcuts import render
from django.http import HttpResponse

from .models import Album, Artist, Contact, Booking

# Create your views here.
def index(request):
   albums = Album.objects.filter(available=True).order_by('-created_at')[:2]
   formatted_albums = ['<li>{}</li>'.format(album.title) for album in albums]
   message = """
      Les deux premiers albums : 
      <ul>
         {}
      </ul>
   """.format("\n".join(formatted_albums))
   return HttpResponse(message)

def listing(request):
   albums = Album.objects.filter(available=True).order_by('-created_at')
   formatted_albums = ['<li>{}</li>'.format(album.title) for album in albums]
   message = """
      Tous les albums : 
      <ul>
         {}
      </ul>
   """.format("\n".join(formatted_albums))
   return HttpResponse(message)

def details(request, album_id):
   album = Album.objects.get(pk=album_id)
   artists =  ", ".join(artist.name for artist in album.artists.all()).capitalize()

   message = f"Le nom de l'album est {album.title}. Il a été écrit par {artists}"
   return HttpResponse(message)

def search(request):
   query = request.GET.get('query')
   if not query :
      message = Album.objects.all()
   else:
      albums = Album.objects.filter(title__icontains = query)

      if not albums.exists():
         albums = Album.objects.filter(artists__name__icontains = query)
      if not albums.exists():
         message = "Pas d'album pour cette recherche !"
      else:
         albums = ["<li>{}</li>".format(album.title) for album in albums]
         message= """
            Voici les albums correspondant à la requête:
            <ul>
               {}
            </ul>
            
         """.format("\n".join(albums))

   return HttpResponse(message)