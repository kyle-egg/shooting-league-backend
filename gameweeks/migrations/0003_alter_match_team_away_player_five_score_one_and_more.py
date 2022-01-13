# Generated by Django 4.0.1 on 2022-01-13 17:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameweeks', '0002_match_name_match_team_away_player_six_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='team_away_player_five_score_one',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='match',
            name='team_away_player_five_score_two',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='match',
            name='team_away_player_four_score_one',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='match',
            name='team_away_player_four_score_two',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='match',
            name='team_away_player_one_score_one',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='match',
            name='team_away_player_one_score_two',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='match',
            name='team_away_player_six_score_one',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='match',
            name='team_away_player_six_score_two',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='match',
            name='team_away_player_three_score_one',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='match',
            name='team_away_player_three_score_two',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='match',
            name='team_away_player_two_score_one',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='match',
            name='team_away_player_two_score_two',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='match',
            name='team_home_player_five_score_one',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='match',
            name='team_home_player_five_score_two',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='match',
            name='team_home_player_four_score_one',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='match',
            name='team_home_player_four_score_two',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='match',
            name='team_home_player_one_score_one',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='match',
            name='team_home_player_one_score_two',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='match',
            name='team_home_player_six_score_one',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='match',
            name='team_home_player_six_score_two',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='match',
            name='team_home_player_three_score_one',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='match',
            name='team_home_player_three_score_two',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='match',
            name='team_home_player_two_score_one',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='match',
            name='team_home_player_two_score_two',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
    ]
