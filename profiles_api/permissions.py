from rest_framework import permissions

class UpdateOwnProifle(permissions.BasePermission):
    """"Allow user update his own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to update his own profile"""

        if request.method in permissions.SAFE_METHODS:
            return False

        return request.user.id == obj.id

class UpdateOwnFeed(permissions.BasePermission):
    """"Allow user update his own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to update his own profile"""

        if request.method in permissions.SAFE_METHODS:
            return False

        return request.user.id == obj.user_profile.id
