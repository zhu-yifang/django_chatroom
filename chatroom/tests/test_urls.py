from django.test import SimpleTestCase
from django.urls import reverse, resolve
from chatroom.views import chat_room_list, chat_room, create_room

class UrlsTest(SimpleTestCase):
    def test_chat_room_list_url_resolves(self):
        url = reverse('chat_room_list')
        self.assertEquals(resolve(url).func, chat_room_list)

    def test_chat_room_url_resolves(self):
        url = reverse('chat_room', args=[1])  # Assuming '1' is a valid room ID
        self.assertEquals(resolve(url).func, chat_room)

    def test_create_room_url_resolves(self):
        url = reverse('create_room')
        self.assertEquals(resolve(url).func, create_room)
