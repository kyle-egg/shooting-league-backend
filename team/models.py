from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(max_length=500)
    logo = models.CharField(max_length=500)
    website = models.CharField(max_length=200)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.TextField(max_length=500)
    players = models.ManyToManyField(
        'player.Player',
        related_name='teams',
        blank=True
    )

    def __str__(self):
        return f'{self.name}'