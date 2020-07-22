from django.db import models

# Create your models here.

### MODELES JSON ------------

ARTISTS = {
  'francis-cabrel': {'name': 'Francis Cabrel'},
  'lej': {'name': 'Elijay'},
  'rosana': {'name': 'Rosana'},
  'maria-dolores-pradera': {'name': 'María Dolores Pradera'},
}


ALBUMS = [
  {'name': 'Sarbacane', 'artists': [ARTISTS['francis-cabrel']]},
  {'name': 'La Dalle', 'artists': [ARTISTS['lej']]},
  {'name': 'Luna Nueva', 'artists': [ARTISTS['rosana'], ARTISTS['maria-dolores-pradera']]}
]


### MODELES SQL ------------

class Artists(models.Model):
  name = models.CharField(max_length=200, unique=True)

class Contact(models.Model):
  name = models.CharField(max_length=200, unique=True)
  email = models.EmailField(max_length=200, unique=True)

class Album(models.Model):
  reference = models.IntegerField(null=True)
  created_at = models.DateField(auto_now_add=True)
  available = models.BooleanField(default=True)
  title = models.CharField(max_length=200)
  picture= models.URLField()

class Booking(models.Model):
  created_at = models.DateField(auto_now_add=True)
  contacted = models.BooleanField(default=False)
  
  # Relations
  album = models.OneToOneField(Album, on_delete= models.DO_NOTHING) # Une reservation par album
  contact = models.ForeignKey(Contact, on_delete=models.CASCADE) # Plusieurs réservation peuvent appartenir à un contact
  artists = models.ManyToManyField(Album, related_name='albums', blank=True)