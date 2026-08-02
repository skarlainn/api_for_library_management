from django.contrib import admin

from books.models import Book, Genre, RentBooks


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "genre",
        "description",
        "quantity",
        "available_quantity",
        "publication_date",
        "publisher",
        "cover_image",
    )


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(RentBooks)
class RentBooksAdmin(admin.ModelAdmin):
    list_display = (
        "book",
        "date_issue",
        "return_date",
        "is_returned",
        "reader",
        "term",
    )
