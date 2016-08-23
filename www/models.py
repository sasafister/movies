from django.db import models

# Create your models here.
class Movies(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField('date published')

    def __str__(self):
        return self.title

class Movie(models.Model):
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.CharField(max_length=255)
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)

    def __str__(self):
        return self.title
