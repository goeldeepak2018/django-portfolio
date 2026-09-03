from django.contrib import admin

from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "is_featured",
        "is_published",
        "created_at",
    )

    list_filter = (
        "is_featured",
        "is_published",
    )

    search_fields = (
        "title",
        "description",
        "technologies",
    )

    prepopulated_fields = {
        "slug": ("title",),
    }