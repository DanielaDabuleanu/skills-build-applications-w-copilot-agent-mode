from django.test import TestCase
from .models import Profile

class ProfileModelTest(TestCase):
    def test_create_profile(self):
        profile = Profile.objects.create(bio='Test bio')
        self.assertEqual(profile.bio, 'Test bio')
