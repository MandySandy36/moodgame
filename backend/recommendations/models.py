from django.db import models

class Game(models.Model):
    name = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    description = models.TextField()
    tags = models.JSONField()  # Store tags like ["calming", "thrilling"]
    rating = models.FloatField()

    def __str__(self):
        return self.name
