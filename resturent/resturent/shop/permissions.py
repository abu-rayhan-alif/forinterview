from rest_framework import permissions

class IsOwnerGroup(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Owners').exists()

class IsEmployeeGroup(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Employees').exists()