from django.urls import path
from .views import ActivityListCreate, ActivityDetail

app_name = 'activities'

urlpatterns = [
    path('activities/', ActivityListCreate.as_view(), name='activity-list'),
    path('activities/<int:pk>/', ActivityDetail.as_view(), name='activity-detail'),
]
