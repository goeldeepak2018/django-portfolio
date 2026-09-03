from django.db import models


class Resume(models.Model):
    title = models.CharField(max_length=150)
    file = models.FileField(upload_to="resume/")
    is_active = models.BooleanField(default=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title