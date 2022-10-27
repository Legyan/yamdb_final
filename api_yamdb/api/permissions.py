from rest_framework import permissions


class IsAdminPermission(permissions.BasePermission):
    """Права доступа: только Администратор"""
    def has_permission(self, request, view):
        return (request.user.is_authenticated and request.user.is_admin)


class IsAuthorOrAdminOrModeratorOrReadOnly(permissions.BasePermission):
    """Доступ для POST, PATCH, DELETE у автора, модератора или администратора.
    Для GET у всех пользователей"""

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user
                or (request.user.is_authenticated
                    and (request.user.is_admin
                         or request.user.is_moderator)))


class AdminOrReadOnly(permissions.BasePermission):
    """POST, PATCH, DELETE у админа.
    У остальных только GET"""
    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or (
                request.user.is_authenticated
                and request.user.is_admin)
        )
