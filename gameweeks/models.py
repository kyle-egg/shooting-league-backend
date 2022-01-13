from django.db import models
from django.core.validators import MaxValueValidator

class Gw(models.Model):
    league = models.ManyToManyField(
        'league.Competition',
        related_name='fixtures',
        blank=True
    )
    date = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.date}'

class Match(models.Model):
    gameweek = models.ForeignKey(
        Gw,
        related_name='matches',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    played = models.BooleanField()
    team_home = models.ManyToManyField(
        'team.Team',
        related_name='home_matches',
        blank=True
    )
    team_home_player_one = models.ManyToManyField(
        'player.Player',
        related_name='home_player_one_matches',
        blank=True
    )
    team_home_player_one_score_one = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(100)], null=True)
    team_home_player_one_score_two = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(100)], null=True)
    team_home_player_two = models.ManyToManyField(
        'player.Player',
        related_name='home_player_two_matches',
        blank=True
    )
    team_home_player_two_score_one = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(100)], null=True)
    team_home_player_two_score_two = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(100)], null=True)
    team_home_player_three = models.ManyToManyField(
        'player.Player',
        related_name='home_player_three_matches',
        blank=True
    )
    team_home_player_three_score_one = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(100)], null=True)
    team_home_player_three_score_two = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(100)], null=True)
    team_home_player_four = models.ManyToManyField(
        'player.Player',
        related_name='home_player_four_matches',
        blank=True
    )
    team_home_player_four_score_one = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(100)], null=True)
    team_home_player_four_score_two = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(100)], null=True)
    team_home_player_five = models.ManyToManyField(
        'player.Player',
        related_name='home_player_five_matches',
        blank=True
    )
    team_home_player_five_score_one = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(100)], null=True)
    team_home_player_five_score_two = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(100)], null=True)     
    team_home_player_six = models.ManyToManyField(
        'player.Player',
        related_name='home_player_six_matches',
        blank=True
    )
    team_home_player_six_score_one = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(100)], null=True)
    team_home_player_six_score_two = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(100)], null=True)     
    team_away = models.ManyToManyField(
        'team.Team',
        related_name='away_matches',
        blank=True
    )
    team_away_player_one = models.ManyToManyField(
        'player.Player',
        related_name='away_player_one_matches',
        blank=True
    )
    team_away_player_one_score_one = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(100)], null=True)
    team_away_player_one_score_two = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(100)], null=True)
    team_away_player_two = models.ManyToManyField(
        'player.Player',
        related_name='away_player_two_matches',
        blank=True
    )
    team_away_player_two_score_one = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(100)], null=True)
    team_away_player_two_score_two = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(100)], null=True)
    team_away_player_three = models.ManyToManyField(
        'player.Player',
        related_name='away_player_three_matches',
        blank=True
    )
    team_away_player_three_score_one = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(100)], null=True)
    team_away_player_three_score_two = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(100)], null=True)
    team_away_player_four = models.ManyToManyField(
        'player.Player',
        related_name='away_player_four_matches',
        blank=True
    )
    team_away_player_four_score_one = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(100)], null=True)
    team_away_player_four_score_two = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(100)], null=True)
    team_away_player_five = models.ManyToManyField(
        'player.Player',
        related_name='away_player_five_matches',
        blank=True
    )
    team_away_player_five_score_one = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(100)], null=True)
    team_away_player_five_score_two = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(100)], null=True)    
    team_away_player_six = models.ManyToManyField(
        'player.Player',
        related_name='away_player_six_matches',
        blank=True
    )
    team_away_player_six_score_one = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(100)], null=True)
    team_away_player_six_score_two = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(100)], null=True)     
    def __str__(self):
        return f'{self.date} - {self.name}'
