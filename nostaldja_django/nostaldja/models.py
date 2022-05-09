from django.db import models


class Decade(models.Model):
    start_year = models.IntegerField()

    def __str__(self):
        return self.start_year


class Fads(models.Model):
    decade = models.ForeignKey(
        Decade, on_delete=models.CASCADE, related_name='fads')
    name = models.CharField(max_length=50)
    image_url = models.TextField()
    description = models.CharField(max_length=300)
