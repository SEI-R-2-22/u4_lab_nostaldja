from unicodedata import name
from django.db import models

# tunr/models.py
class Artist(models.Model):
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    photo_url = models.TextField()

    def __str__(self):
        return self.name

class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='songs')
    title = models.CharField(max_length=100, default='no song title')
    album = models.CharField(max_length=100, default='no album title')
    preview_url = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.title


class Decade(models.Model):
    start_year = models.CharField(max_length=100)

    def __str__(self):
        return self.start_year

class Fad(models.Model):
    name = models.CharField(max_length=100)
    image_url = models.CharField(max_length=200, null=False)
    description = models.CharField(max_length=300, default='No description')
    decade = models.ForeignKey(Decade, on_delete=models.CASCADE)