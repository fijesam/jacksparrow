from django.db import models
from datetime import datetime
import uuid # Required for unique instances
# Create your models here.
class Artiste(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID')
    first_name= models.CharField(max_length=200)
    last_name= models.CharField(max_length=200)
    age=models.PositiveBigIntegerField()

    class Meta:
        ordering=['first_name']

    def _str_(self):
        return self.first_name

class Song(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID')
    artiste = models.ForeignKey('Artiste', on_delete=models.RESTRICT, null=True)
    title= models.CharField(max_length=200)
    date_released= models.DateField(null=True, blank=True)
    likes=models.PositiveBigIntegerField()
    artiste_id = Artiste.id
    # likes=onclick.count/user.count(forms;first = request.POST['first'])

    class Meta:
        ordering=['title']

    def _str_(self):
        return self.title

class Lyric:
    song=models.ForeignKey('Lyric', on_delete=models.SET_NULL, null=True)
    content = models.CharField(max_length=500)
    song_id = Song.id