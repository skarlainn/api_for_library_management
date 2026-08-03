from django.urls import path

from author.apps import AuthorConfig
from author.views import (
    AuthorCreateApiView,
    AuthorRetrieveApiView,
    AuthorUpdateApiView,
    AuthorListApiView,
    AuthorDestroyApiView,
)

app_name = AuthorConfig.name

urlpatterns = [
    path("create/", AuthorCreateApiView.as_view(), name="author-create"),
    path("<int:pk>/", AuthorRetrieveApiView.as_view(), name="author-detail"),
    path("", AuthorListApiView.as_view(), name="authors-list"),
    path("<int:pk>/update", AuthorUpdateApiView.as_view(), name="author-update"),
    path("<int:pk>/delete", AuthorDestroyApiView.as_view(), name="author-delete"),
]
