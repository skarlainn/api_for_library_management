from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=150, verbose_name="Имя автора", help_text="Введите имя автора")
    last_name = models.CharField(max_length=150, verbose_name="Фамилия автора", help_text="Введите фамилию автора")
    date_of_birth = models.DateField(
        verbose_name="Дата рождения автора",
        help_text="Укажите дату рождения в формате YYYY-MM-DD",
        blank=True,
        null=True,
    )
    bio = models.TextField(
        verbose_name="Биография автора", help_text="Напишите биографию автора", blank=True, null=True
    )
    date_of_death = models.DateField(
        verbose_name="Дата смерти автора",
        help_text="Укажите дату смерти в формате YYYY-MM-DD",
        blank=True,
        null=True,
    )
    country = models.CharField(
        max_length=100,
        verbose_name="Страна проживания автора",
        help_text="Укажите страну где проживал автор",
        blank=True,
        null=True,
    )
    language = models.CharField(
        max_length=100,
        verbose_name="Родной язык автора",
        help_text="Укажите родной язык автора",
        blank=True,
        null=True,
    )
    photo = models.ImageField(
        upload_to="author/photo",
        verbose_name="Фото или изображение автора",
        help_text="Загрузите фото или изображение автора",
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"
