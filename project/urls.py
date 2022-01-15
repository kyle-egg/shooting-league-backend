from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/gameweeks/', include('gameweeks.urls')),
    path('api/matches/', include('gameweeks.urls')),
    path('api/players/', include('player.urls')),
    path('api/seasons/', include('league.urls')),
    path('api/teams/', include('team.urls'))
]
