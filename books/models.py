from django.db import models
from author.models import Author
from users.models import User

NULLABLE = {"blank": True, "null": True}



class Genre(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название жанра")
    description = models.TextField(verbose_name="Описание жанра", **NULLABLE)


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
        related_name="genres",
        help_text="Укажите жанр книги",
        **NULLABLE,
    )
    description = models.TextField(verbose_name="Описание книги", **NULLABLE)
    quantity = models.PositiveSmallIntegerField(verbose_name="Количество книг")
    publication_date = models.DateField(verbose_name="Дата публикации", **NULLABLE)
    publisher = models.CharField(max_length=150, verbose_name="Издатель")
    cover_image = models.ImageField(upload_to="books/cover_image", verbose_name="Обложка", **NULLABLE)
    is_available = models.BooleanField(default=True, help_text="Доступна ли книга для выдачи")

    def __str__(self):
        return f"{self.title} - {self.author}"

    class Meta:
        verbose_name = "книга"
        verbose_name_plural = "книги"
        ordering = ["title"]


class RentBooks(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        verbose_name="Книга",
        related_name="books",
        help_text="Укажите книгу которую пользователь берет для чтения",
    )
    date_issue = models.DateField(auto_now_add=True, verbose_name="Дата выдачи книги")
    return_date = models.DateField(verbose_name="Дата возврата книги")
    is_returned = models.BooleanField(default=False, verbose_name="Флаг возврата книги")
    user = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, verbose_name="Читатель книги", help_text="Читатель книги"
    )
    term = models.PositiveSmallIntegerField(verbose_name="Срок аренды", help_text="Срок аренды в днях")

    def __str__(self):
        return f"Книга: {self.book} у {self.user} на {self.term} дней"

    class Meta:
        verbose_name = "Аренда книги"
        verbose_name_plural = "Аренды книг"
        ordering = ["pk"]
