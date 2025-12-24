from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrOperator(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        if not request.user.is_authenticated:
            return False

        return hasattr(request.user, "userprofile") and \
               request.user.userprofile.role in ["ADMIN", "OPERATOR"]

