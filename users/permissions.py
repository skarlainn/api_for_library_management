from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """Ограничивает доступ к ресурсам только для создавших их пользователей"""

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
