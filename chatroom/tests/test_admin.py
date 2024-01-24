from django.test import TestCase
from django.contrib.admin.sites import AdminSite
from chatroom.models import ChatRoom
from chatroom.admin import ChatRoomAdmin

class MockRequest:
    pass

class ChatRoomAdminTest(TestCase):
    def setUp(self):
        self.site = AdminSite()

    def test_admin_str(self):
        admin = ChatRoomAdmin(ChatRoom, self.site)
        self.assertEqual(str(admin), 'chatroom.ChatRoomAdmin')
