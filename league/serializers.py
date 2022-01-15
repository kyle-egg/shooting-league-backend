from rest_framework import serializers

from .models import Season, Competition

class CompetitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competition
        fields = '__all__'

class SeasonSerializer(serializers.ModelSerializer):
    competitions = CompetitionSerializer(many=True, read_only=True)
    
    class Meta:
        model = Season
        fields = '__all__'

