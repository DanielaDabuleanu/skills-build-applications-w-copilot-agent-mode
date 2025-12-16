
from django.urls import path
from .views import (
    UserList, UserDetail,
    ProfileList, ProfileDetail,
    TeamList, TeamDetail,
    LeaderboardList, LeaderboardDetail,
    WorkoutList, WorkoutDetail
)

app_name = 'users'

urlpatterns = [
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('profiles/', ProfileList.as_view(), name='profile-list'),
    path('profiles/<int:pk>/', ProfileDetail.as_view(), name='profile-detail'),
    path('teams/', TeamList.as_view(), name='team-list'),
    path('teams/<int:pk>/', TeamDetail.as_view(), name='team-detail'),
    path('leaderboard/', LeaderboardList.as_view(), name='leaderboard-list'),
    path('leaderboard/<int:pk>/', LeaderboardDetail.as_view(), name='leaderboard-detail'),
    path('workouts/', WorkoutList.as_view(), name='workout-list'),
    path('workouts/<int:pk>/', WorkoutDetail.as_view(), name='workout-detail'),
]
