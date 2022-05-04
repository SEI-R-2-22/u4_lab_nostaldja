from django.db import models

# Create your models here.

class Decade(models.Model):
    start_year = models.CharField(max_length=50)

    def __str__(self):
        return self.start_year
