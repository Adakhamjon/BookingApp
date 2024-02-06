from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user


class IsAdminOrOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and (request.user.is_superuser or hasattr(request.user, 'owner'))

    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser or obj.owner == request.user