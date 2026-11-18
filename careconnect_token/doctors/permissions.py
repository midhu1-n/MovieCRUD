from rest_framework.permissions import BasePermission
class IsAdminUserOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method=="GET":
            return request.user.is_authenticated
        return request.user.is_authenticated and request.user.is_superuser

    #GET  --Authenticated User

    #POST/PUT/DELETE  --Authenticated+Admin user

    # def has_object_permission(self, request, view, obj):
    #     if request.method=="GET":
    #         return request.user.is_authenticated
    #     return request.user.is_authenticated and request.user.is_superuser