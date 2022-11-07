from django.db import models
from datetime import datetime
import uuid # Required for unique instances
# Create your models here.
class Artiste(models.Model):
    id=models.PositiveBigIntegerField(primary_key=True)
    first_name= models.CharField(max_length=200)
    last_name= models.CharField(max_length=200)
    age=models.PositiveBigIntegerField()

    class Meta:
        ordering=['first_name']

    def __str__(self):
        return f'{self.first_name}'

class Song(models.Model):
    id = models.PositiveBigIntegerField(primary_key=True)
    artiste = models.ForeignKey(Artiste, on_delete=models.RESTRICT, null=True)
    title= models.CharField(max_length=200)
    date_released= models.DateField(null=True, blank=True)
    likes=models.PositiveBigIntegerField()
    
    # likes=onclick.count/user.count(forms;first = request.POST['first'])

    class Meta:
        ordering=['artiste']

    def __str__(self):
        return f'{self.title}'

class Lyric(models.Model):
    song=models.ForeignKey(Song, on_delete=models.SET_NULL, null=True)
    content = models.CharField(max_length=500)
    
    def __str__(self):
        return f'{self.content}'