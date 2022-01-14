from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
)

from .models import Season
from .serializers import SeasonSerializer

class SeasonListView(ListCreateAPIView):
    ''' List View for /season GET'''
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer

class SeasonDetailView(RetrieveUpdateDestroyAPIView):
    ''' Detail View for /season/id SHOW UPDATE DELETE'''
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer