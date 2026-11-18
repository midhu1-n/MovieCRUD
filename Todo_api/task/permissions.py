from rest_framework.permissions import BasePermission
class Custom(BasePermission):
    # def has_permission(self, request, view):
    #     if request.method=="GET":
    #         return request.user.is_authenticated
    #     return request.user.is_authenticated
    def has_object_permission(self, request, view, obj):
        return obj.user==request.user