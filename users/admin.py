from django.contrib import admin
from .models import Profile

# Option 1: Simple registration without customization
# admin.site.register(Profile)

# Option 2: Customized admin view
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'profile_picture')  # Customize the fields to display in the list view
    search_fields = ('user__username', 'bio')  # Add search functionality
    list_filter = ('user__is_staff', 'user__is_active')  # Add filters

    # You can add more customization as needed

admin.site.register(Profile, ProfileAdmin)
