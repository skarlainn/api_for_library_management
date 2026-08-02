from django.utils import timezone
from celery import shared_task
from books.models import RentBooks
from books.services import send_email


@shared_task
def check_return_book():
    """Проверяет дату истечения срока и отправляет читателю письмо если срок пользования книги закончился"""
    rents_books = RentBooks.objects.filter(deadline__lt=timezone.now(), is_returned=False)
    for rent in rents_books:
        send_email(rent)