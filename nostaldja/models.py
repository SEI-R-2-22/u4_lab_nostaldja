from django.db import models

# Create your models here.
# tunr/models.py


class Decades(models.Model):
    start_year = models.CharField(max_length=100)

    def __str__(self):
        return self.start_year


class Fads(models.Model):
    decade = models.ForeignKey(
        Decades, on_delete=models.CASCADE, related_name='fads')
    name = models.CharField(max_length=100, default='no fad name')
    description = models.CharField(max_length=300, default='no description')
    image_url = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name
