from django.db import models

# Create your models here.
class lyrics(models.Model):
    name = models.CharField(max_length=200)
    lyrics = models.TextField()

    def __str__(self):
        return self.name