from rest_framework import serializers

from .models import Match
from team.models import Team
from player.models import Player
from league.models import Competition


class NestedPlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'

class NestedTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

class NestedCompetitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competition
        fields = '__all__'

class MatchSerializer(serializers.ModelSerializer):
  league = NestedCompetitionSerializer(many=True, read_only=True)  
  team_home = NestedTeamSerializer(many=True, read_only=True)
  team_away = NestedTeamSerializer(many=True, read_only=True)
  team_home_player_one = NestedPlayerSerializer(many=True, read_only=True)
  team_home_player_two = NestedPlayerSerializer(many=True, read_only=True)
  team_home_player_three = NestedPlayerSerializer(many=True, read_only=True)
  team_home_player_four = NestedPlayerSerializer(many=True, read_only=True)
  team_home_player_five = NestedPlayerSerializer(many=True, read_only=True)
  team_home_player_six = NestedPlayerSerializer(many=True, read_only=True)
  team_away_player_one = NestedPlayerSerializer(many=True, read_only=True)
  team_away_player_two = NestedPlayerSerializer(many=True, read_only=True)
  team_away_player_three = NestedPlayerSerializer(many=True, read_only=True)
  team_away_player_four = NestedPlayerSerializer(many=True, read_only=True)
  team_away_player_five = NestedPlayerSerializer(many=True, read_only=True)
  team_away_player_six = NestedPlayerSerializer(many=True, read_only=True)

  
  class Meta:
        model = Match
        fields = '__all__'

