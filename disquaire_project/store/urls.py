from django.urls import path

from . import views

app_name = 'store'
urlpatterns = [
   path('', views.listing, name='listing'),
   path('<int:album_id>/', views.details, name='details'),
   path('search/', views.search, name='search')
]