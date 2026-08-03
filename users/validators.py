from rest_framework.exceptions import ValidationError
from django.core.validators import RegexValidator


class PhoneNumberValidator:
    """Валидатор номера телефона с поддержкой международного формата"""

    def __init__(self, field_name):
        self.field_name = field_name
        # Регулярное выражение для международного формата (+79991234567)
        self.international_regex = RegexValidator(
            regex=r"^\+?7?\d{10}$",
            message="Номер телефона должен быть в формате '+79991234567' или '89991234567'",
        )

    def __call__(self, instance):
        phone = instance.get(self.field_name)

        # if not phone:
        #     raise ValidationError(f"Поле {self.field_name} не может быть пустым")
        if phone:
            # Проверка на корректность формата
            try:
                self.international_regex(phone)
            except ValidationError as e:
                raise ValidationError({self.field_name: str(e)})
