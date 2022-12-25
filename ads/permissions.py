from rest_framework.permissions import BasePermission

from users.models import UserRoles


class IsSelectionOwner(BasePermission):
    message = " У вас нет доступа к этой информации"

    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner:
            return True
        else:
            return False


class IsAdOwnerOrStaff(BasePermission):
    message = " У вас нет доступа к этому объявлению"

    def has_object_permission(self, request, view, obj):
        if request.user == obj.author or request.user.role in [UserRoles.ADMIN, UserRoles.MODERATOR]:
            return True
        else:
            return False
