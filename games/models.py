from django.db import models

class Developer(models.Model):
    company_name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    language = models.CharField(max_length=100)

    def __str__(self):
        return self.company_name

class Genres(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Game(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField()
    is_free = models.BooleanField()
    developer = models.ForeignKey(
        Developer,
        on_delete=models.CASCADE,
        related_name="games"
    )

    genres = models.ManyToManyField(
        Genres,
        related_name="games"
    )

    def __str__(self):
        return self.title

