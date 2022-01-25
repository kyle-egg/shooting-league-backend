from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
)

from .models import Match
from .serializers import MatchSerializer

class MatchListView(ListCreateAPIView):
    ''' List View for /matches GET'''
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

class MatchDetailView(RetrieveUpdateDestroyAPIView):
    ''' Detail View for /matchess/id SHOW UPDATE DELETE'''
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

