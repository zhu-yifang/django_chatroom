from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(
        default="default.jpg", upload_to="profile_pics", blank=True
    )
    bio = models.TextField(max_length=500, blank=True)
    last_seen = models.DateTimeField(null=True, blank=True)

    # New fields
    online_status = models.BooleanField(
        default=False
    )  # Indicates if the user is currently online

    def __str__(self):
        return self.user.username

    # Additional methods as needed
