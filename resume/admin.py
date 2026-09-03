from django.contrib import admin

from .models import Resume


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "is_active",
        "uploaded_at",
    )

    list_filter = (
        "is_active",
        "uploaded_at",
    )

    search_fields = (
        "title",
    )

    readonly_fields = (
        "uploaded_at",
    )