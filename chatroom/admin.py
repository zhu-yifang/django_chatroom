from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import ChatRoom, ChatMessage


class ChatRoomAdmin(admin.ModelAdmin):
    # Display the clickable name in the admin page
    list_display = ("id", "name_link")
    readonly_fields = ("id",)  # Display 'id' as a read-only field
    fields = ("id", "name")  # Include 'id' in the fields list

    def name_link(self, obj):
        return format_html(
            '<a href="{}">{}</a>',
            reverse("admin:chatroom_chatroom_change", args=(obj.pk,)),
            obj.name,
        )

    name_link.short_description = "Name"  # Column header for the clickable name


# If you haven't already created an admin class for ChatMessage
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = (
        "content",
        "user",
        "room",
        "timestamp",
    )  # Fields to display in the list view
    list_filter = ("user", "room")  # Fields to filter by in the admin
    search_fields = ("content",)  # Fields to search in the admin

admin.site.register(ChatMessage, ChatMessageAdmin)
admin.site.register(ChatRoom, ChatRoomAdmin)
