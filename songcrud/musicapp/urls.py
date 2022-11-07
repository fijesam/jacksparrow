from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('songs/', views.songlist, name='songs-list'),
    path('songs/<int:id>', views.lyrics, name='song-lyric'),
]