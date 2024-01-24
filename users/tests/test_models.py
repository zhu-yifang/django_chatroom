from django.test import TestCase
from django.contrib.auth.models import User
from users.models import Profile

class ProfileModelTest(TestCase):
    def setUp(self):
        User.objects.create_user(username='testuser', password='12345')

    def test_profile_creation(self):
        user = User.objects.get(username='testuser')
        self.assertTrue(Profile.objects.filter(user=user).exists())

    # Add more tests for custom methods if any
