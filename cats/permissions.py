# from rest_framework import permissions

# class OwnerOrReadOnly(permissions.BasePermission):

#     def has_permission(self, request, view):
#         return (
#                 request.method in permissions.SAFE_METHODS
#                 or request.user.is_authenticated
#             )

#     def has_object_permission(self, request, view, obj):
#         return obj.owner == request.user 


# class ReadOnly(permissions.BasePermission):

#     def has_permission(self, request, view):
#         return request.method in permissions.SAFE_METHODS 

from rest_framework import permissions

class OwnerOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return (
                request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated
            )

    def has_object_permission(self, request, view, obj):
        # Если пользователь аутентифицирован, и он является владельцем объекта,
        # или если это безопасный метод, разрешить доступ.
        if request.user.is_authenticated:
            return obj.owner == request.user or request.method in permissions.SAFE_METHODS
        # Если пользователь не аутентифицирован, разрешить только безопасные методы.
        return request.method in permissions.SAFE_METHODS
    