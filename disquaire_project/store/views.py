from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Album, Artist, Contact, Booking

# Create your views here.
def index(request):
   albums = Album.objects.filter(available=True).order_by('-created_at')
   formatted_albums = ['<li>{}</li>'.format(album.title) for album in albums]
   # message = """
   #    Les deux premiers albums : 
   #    <ul>
   #       {}
   #    </ul>
   # """.format("\n".join(formatted_albums))

   template = loader.get_template('store/index.html')
   context = {
      'albums': albums
   }
   return render(request, 'store/index.html', context)

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
   artists = ", ".join(artist.name for artist in album.artists.all()).capitalize()
   context = {
      'album' : album,
      'artists' : artists
   }
   return render(request, 'store/details.html', context)

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