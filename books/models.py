from django.db import models
from isort.place import module_with_reason

from author.models import Author

NULLABLE = {"blank": True, "null": True}


class Book(models.Model):
    title = models.CharField(
        max_length=150,
        verbose_name="Название книги",
        help_text="Укажите название книги",
    )
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="authors",
        verbose_name="Автор",
        help_text="Укажите автора книги",
    )
    genre = models.CharField(max_length=150, verbose_name="Жанр книги", help_text="Укажите жанр", **NULLABLE)
    description = models.TextField(verbose_name="Описание книги", **NULLABLE)
    quantity = models.PositiveSmallIntegerField(verbose_name="Количество книг")
    publication_date = models.DateField(verbose_name="Дата публикации", **NULLABLE)
    publisher = models.CharField(max_length=150, verbose_name="Издатель")