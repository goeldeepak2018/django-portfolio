from django.db import models


class SiteSetting(models.Model):
    site_name = models.CharField(max_length=150)
    tagline = models.CharField(max_length=255, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.site_name