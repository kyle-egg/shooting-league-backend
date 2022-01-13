from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return f'{self.name}'
