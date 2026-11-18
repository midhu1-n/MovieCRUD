
from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):

    def has_object_permission(self, request, view, obj):

        #object level permission
        #if obj.user==request.user
        #   return true
        if request.method=="GET":#Any user can read
            return True

        return obj.user==request.user #only creator of the object can update/delete

#condition obj,user==request.user checks whether the creator of the object and requested user are same