from django.db import models
from django.contrib.auth.models import AbstractUser

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True, verbose_name="Email", help_text="Укажите адрес электронной почты"
    )
    phone = models.CharField(
        max_length=50,
        verbose_name="Номер телефона",
        help_text="Укажите актуальный номер телефона",
        **NULLABLE
    )
    city = models.CharField(max_length=50, verbose_name="Город проживания", **NULLABLE)
    street = models.CharField(max_length=50, verbose_name="Улица", **NULLABLE)
    house_number = models.CharField(
        max_length=10, verbose_name="Номер дома", **NULLABLE
    )
    apartment_number = models.CharField(
        max_length=10, verbose_name="Номер квартиры", **NULLABLE
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
