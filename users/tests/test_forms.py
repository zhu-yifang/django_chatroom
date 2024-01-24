from django.test import TestCase
from users.forms import UserRegisterForm


class UserRegisterFormTest(TestCase):
    def test_form_valid(self):
        form_data = {
            "username": "testuser",
            "email": "test@example.com",
            "password1": "Testing321",
            "password2": "Testing321",
        }
        form = UserRegisterForm(data=form_data)
        if not form.is_valid():
            print(form.errors)
        self.assertTrue(form.is_valid())

    def test_form_invalid(self):
        form = UserRegisterForm(data={})
        self.assertFalse(form.is_valid())
