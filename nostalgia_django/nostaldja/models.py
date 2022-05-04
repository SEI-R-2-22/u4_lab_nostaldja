from django.db import models


class Decade(models.Model):
    start_year = models.CharField(max_length=100)
   
    def __str__(self):
        return self.start_year
    
class Fads(models.Model):
    name = models.ForeignKey(Decade, on_delete=models.CASCADE, related_name='fads')
    imageUrl = models.TextField()
    description = models.CharField(max_length=100)
    decade = models.CharField(max_length=200, null=True)

   
    def __str__(self):
        return self.name
