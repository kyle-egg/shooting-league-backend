# Generated by Django 4.0.1 on 2022-01-18 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0001_initial'),
        ('gameweeks', '0004_alter_match_team_away_player_five_score_one_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='gameweek',
        ),
        migrations.RemoveField(
            model_name='match',
            name='name',
        ),
        migrations.AddField(
            model_name='match',
            name='league',
            field=models.ManyToManyField(blank=True, related_name='fixtures', to='league.Competition'),
        ),
        migrations.DeleteModel(
            name='Gw',
        ),
    ]
