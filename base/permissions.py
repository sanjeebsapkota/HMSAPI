from rest_framework import permissions

class IsDoctor(permissions.BasePermission):
    """
    Custom permission to only allow doctors to access specific views.
    """
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Doctor').exists()

class IsManager(permissions.BasePermission):
    """
    Custom permission to only allow managers to access specific views.
    """
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Manager').exists()

class IsNurse(permissions.BasePermission):
    """
    Custom permission to only allow nurses to access specific views.
    """
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Nurse').exists()

class IsStaff(permissions.BasePermission):
    """
    Custom permission to only allow staff to access specific views.
    """
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Staff').exists()

class IsReceiptionist(permissions.BasePermission):
    """
    Custom permission to only allow staff to access specific views.
    """
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Receiptionist').exists()