from rest_framework import permissions
# from users.models import User

class IsAdminOrRestaurantOwnerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        user = request.user
        return user.is_authenticated and (user.is_staff or user.role == 'Restaurant_Owner')

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        user = request.user
        if user.is_staff:
            return True
        return obj.restaurant.owner == user