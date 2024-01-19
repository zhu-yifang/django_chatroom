from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import ChatRoom, ChatMessage


class ChatRoomAdmin(admin.ModelAdmin):
    # Display the clickable name in the admin page
    list_display = ('id', 'name_link')
    readonly_fields = ('id',)  # Display 'id' as a read-only field
    fields = ('id', 'name')    # Include 'id' in the fields list

    def name_link(self, obj):
        return format_html('<a href="{}">{}</a>', reverse("admin:chatroom_chatroom_change", args=(obj.pk,)), obj.name)
    
    name_link.short_description = 'Name'  # Column header for the clickable name

admin.site.register(ChatMessage)
admin.site.register(ChatRoom, ChatRoomAdmin)
