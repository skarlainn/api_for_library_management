from django.db import models

from author.models import Author

NULLABLE = {"blank": True, "null": True}


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название категории")
    description = models.TextField(verbose_name="Описание категории", **NULLABLE)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]


class Genre(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название жанра")
    description = models.TextField(verbose_name="Описание жанра", **NULLABLE)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, verbose_name="Категория", **NULLABLE
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"
        ordering = ["name"]


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
    genre = models.ForeignKey(
        Genre,
        on_delete=models.SET_NULL,
        verbose_name="Жанр книги",
        help_text="Укажите жанр книги",
        **NULLABLE,
    )
    description = models.TextField(verbose_name="Описание книги", **NULLABLE)
    quantity = models.PositiveSmallIntegerField(verbose_name="Количество книг")
    publication_date = models.DateField(verbose_name="Дата публикации", **NULLABLE)
    publisher = models.CharField(max_length=150, verbose_name="Издатель")

    def __str__(self):
        return f"{self.title} - {self.author}"

    class Meta:
        verbose_name = "книга"
        verbose_name_plural = "книги"
        ordering = ["title"]
