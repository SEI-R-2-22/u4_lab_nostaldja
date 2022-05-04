from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Decade(models.Model):
  start_year = models.CharField(max_length=50)
  description = models.TextField(default='No description.')
  comments = models.TextField(default='No comments.')

  def __str__(self):
    return str(self.start_year)


class Fad(models.Model):
  decade = models.ForeignKey(Decade,
    on_delete=models.CASCADE, 
    related_name='fads')
  name = models.CharField(max_length=100)
  description = models.TextField()
  image_url = models.CharField(max_length=512)

  def __str__(self):
    return self.name