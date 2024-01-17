from django.urls import path
from . import views


urlpatterns = [
    path("rooms/", views.chat_room_list, name="chat_room_list"),
    path("room/<int:room_id>/", views.chat_room, name="chat_room"),
    path("create/", views.create_room, name="create_room"),
]
