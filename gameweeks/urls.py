from django.urls import path
from .views import (
    GwListView,
    GwDetailView,
    MatchListView,
    MatchDetailView
)

urlpatterns = [
    path('', GwListView.as_view()),
    path('<int:pk>/', GwDetailView.as_view()),
    path('<int:gw_pk>/matches/', MatchListView.as_view()),
    path('<int:gw_pk>/matches/<int:match_pk>', MatchDetailView.as_view()),
]
