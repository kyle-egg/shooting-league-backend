from rest_framework import serializers

from .models import Gw

class GwSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gw
        fields = '__all__'