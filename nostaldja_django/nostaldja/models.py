from django.db import models

# Create your models here.
class Decade(models.Model):
    start_year = models.CharField(max_length=100)

    def __str__(self):
        return self.start_year

class Fad(models.Model):
    name = models.CharField(max_length=100)
    image_url = models.CharField(max_length=500, null=True)
    description = models.CharField(max_length=1000, default='no description')
    decade= models.ForeignKey(Decade, on_delete=models.CASCADE, related_name='fad')

    def __str__(self):
        return self.name
