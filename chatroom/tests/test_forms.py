from django.test import TestCase
from chatroom.forms import ChatRoomForm

class ChatRoomFormTest(TestCase):
    def test_form_valid(self):
        form_data = {'name': 'Test Room'}
        form = ChatRoomForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid(self):
        form = ChatRoomForm(data={})
        self.assertFalse(form.is_valid())
