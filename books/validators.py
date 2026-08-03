from rest_framework.exceptions import ValidationError
from datetime import datetime, date


class DeadlineValidator:
    """Валидатор для проверки корректности дат начала и конца аренды книги"""

    def __init__(self, start_field, end_field):
        self.start_field = start_field
        self.end_field = end_field

    def __call__(self, instance):
        start_date = instance.get(self.start_field)
        end_date = instance.get(self.end_field)

        # Проверка на None значения
        if start_date is None or end_date is None:
            raise ValidationError(
                f"Обе даты должны быть указаны. {self.start_field} и {self.end_field} не могут быть пустыми."
            )

        # Проверка типа данных
        if not isinstance(start_date, (date, str)) or not isinstance(
            end_date, (date, str)
        ):
            raise ValidationError(
                f"Значения полей {self.start_field} и {self.end_field} должны быть датами"
            )

        # Преобразование строковых значений в datetime при необходимости
        start_date = (
            start_date.date() if isinstance(start_date, datetime) else start_date
        )
        end_date = end_date.date() if isinstance(end_date, datetime) else end_date

        # Основная проверка
        if end_date <= start_date:
            raise ValidationError(
                {
                    self.end_field: "Дата возврата должна быть позже даты выдачи",
                    self.start_field: "Дата выдачи должна быть раньше даты возврата",
                }
            )
