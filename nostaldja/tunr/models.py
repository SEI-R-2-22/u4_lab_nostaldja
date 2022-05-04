from pydoc import describe
from django.db import models

# Create your models here.
class Decades(models.Model):
  start_year = models.CharField(max_length=100)


class Fads(models.Model):
  name = models.CharField(max_length=100)
  image_url = models.CharField(max_length=200, null=True)
  description = models.TextField()
  decade = models.ForeignKey(Decades, on_delete=models.PROTECT, null=True)