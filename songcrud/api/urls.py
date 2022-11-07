from django.urls import path
from .views import song_list_api

urlpatterns = [
    path('songs/', song_list_api, name='song_list_api'),
    path('songs/<int:id>', song_list_api, name='song_detail_api'),
]