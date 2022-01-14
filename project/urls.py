from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gameweeks/', include('gameweeks.urls')),
    path('players/', include('player.urls')),
    path('seasons/', include('league.urls')),
    path('teams/', include('team.urls'))
]
