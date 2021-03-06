from django.db import models
from django.db.models.deletion import CASCADE

class Review(models.Model):
    game = models.ForeignKey("Game", on_delete=CASCADE)
    player = models.ForeignKey("Player", on_delete=CASCADE)
    review = models.TextField()