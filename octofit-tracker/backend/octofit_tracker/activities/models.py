from django.db import models
from django.conf import settings


class Activity(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='activities')
    name = models.CharField(max_length=200)
    duration = models.IntegerField(help_text='Duration in minutes')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.user}) - {self.duration}m"
