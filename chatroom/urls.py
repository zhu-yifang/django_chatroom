from django.contrib.auth import views as auth_views
from django.urls import path
from . import views


urlpatterns = [
    path("rooms/", views.chat_room_list, name="chat_room_list"),
    path("room/<int:room_id>/", views.chat_room, name="chat_room"),
    path("create/", views.create_room, name="create_room"),
    # Login and logout URLs using Django's built-in views
    path(
        "login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"
    ),
    path("logout/", auth_views.LogoutView.as_view(next_page="/"), name="logout"),
    # Registration URL
    path("register/", views.register, name="register"),
]
