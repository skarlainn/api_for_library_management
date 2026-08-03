# DF1 API для управления библиотекой

## Описание проекта

Система предоставляет REST API для управления библиотечным каталогом, включая функции работы с книгами, пользователями и
процессом выдачи книг. Проект построен на фреймворке Django с использованием Django REST Framework и JWT для аутентификации.

## Стек технологий:
- Backend: Django, Django REST Framework
- База данных: PostgreSQL
- Аутентификация: JWT (используя djangorestframework-simplejwt)
- Контейнеризация: Docker, Docker Compose
- Документация API: OpenAPI (Swagger / ReDoc)
- Формат кода: PEP8

## Основной функционал:

- Управление книгами (создание, редактирование, удаление, поиск по различным критериям).
- Управление авторами (создание, редактирование, удаление).
- Управление пользователями (регистрация, авторизация, получение информации).
- Выдача и возврат книг.
- Аутентификация с помощью JWT (JSON Web Tokens).
- Отслеживание статуса возврата книги с помощью Celery-beat с отправкой уведомления об истечении срока пользования книгой


## Установка

1. Клонируйте репозиторий

```bash
git clone https://github.com/skarlainn/api_for_library_management.git
```

2. Установите зависимости

```bash
poetry install
```

3. Заполните файл .env используя шаблон .env.sample

4. Примените миграции

```bash
python manage.py migrate
```

5. Создайте суперпользователя

```bash
python manage.py csu
```

6. Заполните БД тестовыми данными
```bash
python manage.py loaddata author_fixture.json
python manage.py loaddata books_fixture.json
```
7. Запустите проект
```bash
python manage.py runserver
```
8. Для работы Celery убедитесь, что у Вас установлен и запущен Redis
9. Выполните команды:
```bash
celery -A config worker -l INFO -P eventlet
celery -A config beat -l INFO
```

## Запуск с помощью Docker
1. Убедитесь что у Вас установлен и запущен Docker
2. Перейдите в корень проекта:
```bash
cd api_for_library_management
```
3. Выполните команду:
```bash 
docker_compose up -d --build
```
4. Дождитесь завершения процесса сборки и запуска контейнеров
5. Создайте суперпользователя:
```bash
docker-compose exec app python manage.py csu
```
5. Приложение доступно по адресу: http://127.0.0.1:8000

## Документация доступна по адресу:
http://127.0.0.1:8000/swager/
http://127.0.0.1:8000/redoc/

