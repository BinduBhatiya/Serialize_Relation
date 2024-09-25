from django.db import models

# Create your models here.
class Singre(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name 

class Song(models.Model):
    title = models.CharField(max_length=50)
    singre = models.ForeignKey(Singre, on_delete=models.CASCADE, related_name="song")
    duration = models.IntegerField()

    def __str__(self):
        return self.title
    