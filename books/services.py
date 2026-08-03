from datetime import date

from django.core.mail import send_mail
from rest_framework.exceptions import ValidationError

from config.settings import EMAIL_HOST_USER


def return_book(rent_book, book):
    """Отмечает книгу как возвращенную"""
    if not rent_book.is_returned:
        rent_book.is_returned = True
        rent_book.return_date = date.today()
        if book.available_quantity < book.quantity:
            book.available_quantity += 1
            book.is_available = True
            book.save()
            rent_book.save()
        else:
            raise ValidationError("Все книги уже на месте")
    else:
        raise ValidationError(f"Книга {book.title} уже возвращена")
    return book, rent_book


def take_book(book):
    """Отмечает книгу как выданную"""
    if book.is_available:
        if book.available_quantity >= 1:
            book.available_quantity -= 1
            book.save()
        else:
            book.is_available = False
            book.save()
        return book
    else:
        raise ValidationError(f"Книга {book.title} отсутствует в наличии.")


def send_email(obj):
    """Отправка письма с напоминанием о возврате книги"""
    subject = "Закончился срок пользования книги"
    message = (
        f"Уважаемые читатель!"
        f"\n\nИнформируем Вас о том, что срок пользования книгой {obj.book} подходит к концу. "
        f"Согласно правилам библиотеки, срок возврата указанного издания истекает {obj.deadline}."
        "\nПросим сделать это своевременно для обеспечения доступа к изданию другим читателям."
    )
    from_email = EMAIL_HOST_USER
    recipient_list = [obj.user.email]
    send_mail(subject, message, from_email, recipient_list)
