from django.urls import path
from . import views
from django.views.generic.base import RedirectView


urlpatterns = [
    path(
        "", RedirectView.as_view(url="rooms/", permanent=False), name="index"
    ),  # Redirect from root to /rooms
    path("rooms/", views.chat_room_list, name="chat_room_list"),
    path("room/<int:room_id>/", views.chat_room, name="chat_room"),
    path("create-room/", views.create_room, name="create_room"),
    path('room/<int:room_id>/post_message/', views.post_message, name='post_message'),
]
