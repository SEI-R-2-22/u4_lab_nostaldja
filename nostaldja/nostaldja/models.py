from django.db import models

class Decade(models.Model):
    start_year = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.start_year

class Fad(models.Model):
    name = models.CharField(max_length=100, default='no fad name')
    image_url = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, default='no description')
    decade = models.ForeignKey(Decade, on_delete=models.CASCADE, related_name='fads')

    def __str__(self):
        return self.name