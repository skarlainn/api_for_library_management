from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("books/", include("books.urls", namespace="books")),
    path("users/", include("users.urls", namespace="users")),
    path("authors/", include("author.urls", namespace="authors")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

