from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import SongSerializer
from musicapp.models import Song

# Create your views here.

@csrf_exempt
def song_list_api(request):
    if request.method =="GET":
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method =="POST":
        data = JSONParser().parse(request)
        serializer = SongSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

def song_detail_api(request,id):
    try:
        song = Song.objects.get(id=id)
    except Song.DoesNotExist:
        return JsonResponse({"error":"Song not found"}, status=400)
    if request.method =="GET":
        serializer = SongSerializer(song)
        return JsonResponse(serializer.data)
    if request.method =="PUT":
        data = JSONParser().parse(request)
        serializer = SongSerializer(song, data=data)
        if serializer.is_valid():
            serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)
    if request.method == "DELETE":
        song.delete()
        return JsonResponse({"message":"Song deleted"}, status=204)
