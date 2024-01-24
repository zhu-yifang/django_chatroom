from django.test import TestCase
from django.contrib.admin.sites import AdminSite
from users.models import Profile
from users.admin import ProfileAdmin

class MockRequest:
    pass

class ProfileAdminTest(TestCase):
    def setUp(self):
        self.site = AdminSite()

    def test_admin_str(self):
        admin = ProfileAdmin(Profile, self.site)
        self.assertEqual(str(admin), 'users.ProfileAdmin')
