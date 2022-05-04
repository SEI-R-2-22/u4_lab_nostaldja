from django.db import models

# Create your models here.


class Decade(models.Model):
    start_year = models.IntegerField()


class Fad(models.Model):
    name = models.CharField(max_length=50)
    image_url = models.TextField()
    description = models.TextField()
    decade = models.CharField(max_length=10)
