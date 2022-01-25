from django.db import models

class Season(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return f'{self.name}'


class Competition(models.Model):
    season = models.ForeignKey(
        Season,
        related_name='competitions',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return f'{self.season} - {self.name}'
