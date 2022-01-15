from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
)

from .models import Gw, Match
from .serializers import GwSerializer, MatchSerializer

class GwListView(ListCreateAPIView):
    ''' List View for /gameweeks GET'''
    queryset = Gw.objects.all()
    serializer_class = GwSerializer

class GwDetailView(RetrieveUpdateDestroyAPIView):
    ''' Detail View for /gameweeks/id SHOW UPDATE DELETE'''
    queryset = Gw.objects.all()
    serializer_class = GwSerializer

class MatchListView(ListCreateAPIView):
    ''' List View for /matchess GET'''
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

class MatchDetailView(RetrieveUpdateDestroyAPIView):
    ''' Detail View for /matchess/id SHOW UPDATE DELETE'''
    queryset = Match.objects.all()
    serializer_class = MatchSerializer