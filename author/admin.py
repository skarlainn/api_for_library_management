from django.contrib import admin

from .models import Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "date_of_birth",
        "bio",
        "date_of_death",
        "country",
        "language",
        "photo",
    )
