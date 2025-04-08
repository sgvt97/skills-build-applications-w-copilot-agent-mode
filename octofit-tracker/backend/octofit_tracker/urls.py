"""
URL configuration for octofit_tracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

import logging
from django.contrib import admin
from django.urls import path, include
from .views import UserViewSet, TeamViewSet, ActivityViewSet, LeaderboardViewSet, WorkoutViewSet, api_root

# Add debug logging to confirm requests are reaching the views
logging.basicConfig(level=logging.INFO)

urlpatterns = [
    path('api/', include([
        path('users/', UserViewSet.as_view({'get': 'list'}), name='user-list'),
        path('users/<str:pk>/', UserViewSet.as_view({'get': 'retrieve'}), name='user-detail'),
        path('teams/', TeamViewSet.as_view({'get': 'list'}), name='team-list'),
        path('teams/<str:pk>/', TeamViewSet.as_view({'get': 'retrieve'}), name='team-detail'),
        path('activities/', ActivityViewSet.as_view({'get': 'list'}), name='activity-list'),
        path('activities/<str:pk>/', ActivityViewSet.as_view({'get': 'retrieve'}), name='activity-detail'),
        path('leaderboard/', LeaderboardViewSet.as_view({'get': 'list'}), name='leaderboard-list'),
        path('leaderboard/<str:pk>/', LeaderboardViewSet.as_view({'get': 'retrieve'}), name='leaderboard-detail'),
        path('workouts/', WorkoutViewSet.as_view({'get': 'list'}), name='workout-list'),
        path('workouts/<str:pk>/', WorkoutViewSet.as_view({'get': 'retrieve'}), name='workout-detail'),
    ])),
    path('', api_root, name='api-root'),  # Root endpoint
    path("admin/", admin.site.urls),
]

logging.info("URL patterns loaded successfully.")
