from django.shortcuts import render
from .models import Song, Artiste, Lyric
from django.views import generic
from django.shortcuts import get_object_or_404
#imported HttpResponse, HttpResponseRedirect, reverse and datetime for Comments
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from datetime import datetime

# Create your views here.

def index(request):
    """View function for home page of site."""

    num_songs = Song.objects.all().count()

    context = {
        'num_songs': num_songs,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

def songlist(request):
    """View function for home page of site."""

    songs = Song.objects.all()

    context = {
        'songs': songs,
    }

        # Render the HTML template index.html with the data in the context variable
    return render(request, 'musicapp/songlist.html', context=context)

def lyrics(request, id):
    """View function for home page of site."""

    song= Song.objects.get(id=id)

    context = {
        'song': song,
    }

        # Render the HTML template index.html with the data in the context variable
    return render(request, 'musicapp/lyrics.html', context=context)
