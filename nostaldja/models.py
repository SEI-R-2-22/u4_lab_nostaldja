from pyexpat import model
from django.db import models

# Create your models here.
class Decade(models.Model):
    start_year = models.TextField()

    def __str__(self):
        return self.start_year

class Fad(models.Model):
    name = models.TextField()
    image_url = models.TextField()
    description = models.TextField()
    decade = models.ForeignKey(Decade, on_delete=models.CASCADE, related_name='decade')

    def __str__(self):
        return self.name