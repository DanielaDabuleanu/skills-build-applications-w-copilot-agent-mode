from django.test import TestCase
from .models import Activity

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        activity = Activity.objects.create(name='Test', duration=10)
        self.assertEqual(activity.name, 'Test')
        self.assertEqual(activity.duration, 10)
