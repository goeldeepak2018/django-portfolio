from django.contrib import admin

from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "headline",
        "email",
        "location",
    )

    search_fields = (
        "name",
        "headline",
        "email",
        "summary",
    )

    fieldsets = (
        (
            "Basic Information",
            {
                "fields": (
                    "name",
                    "headline",
                    "summary",
                    "profile_image",
                )
            },
        ),
        (
            "Contact Information",
            {
                "fields": (
                    "email",
                    "phone",
                    "location",
                )
            },
        ),
    )