from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=150)
    headline = models.CharField(max_length=255)
    summary = models.TextField()
    profile_image = models.ImageField(
        upload_to="profile/",
        blank=True,
        null=True,
    )
    location = models.CharField(max_length=150, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.name