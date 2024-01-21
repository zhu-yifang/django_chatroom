from django.contrib.auth.models import User
from django.db import models
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(default="default.jpg", upload_to="profile_pics")
    bio = models.TextField(max_length=500, blank=True)
    last_seen = models.DateTimeField(null=True, blank=True)

    # New fields
    online_status = models.BooleanField(
        default=False
    )  # Indicates if the user is currently online

    def __str__(self):
        return self.user.username

    def save(self):
        super().save()

        # Resize the profile picture if it's too large
        img = Image.open(self.profile_picture.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profile_picture.path)
