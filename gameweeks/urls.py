from django.urls import path
from .views import (
    GwListView,
    GwDetailView
)

urlpatterns = [
    path('', GwListView.as_view()),
    path('<int:pk>/', GwDetailView.as_view()),
]
