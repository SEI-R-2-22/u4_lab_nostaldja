from django.db import models

# Create your models here.


class Decade(models.Model):
    start_year = models.CharField(max_length=10)


class Fad(models.Model):
    name = models.CharField(max_length=50)
    image_url = models.TextField()
    description = models.TextField()
    decade = models.ForeignKey(
        Decade, on_delete=models.CASCADE, related_name='fads')
