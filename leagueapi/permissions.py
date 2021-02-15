from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='ADMIN').exists()


class IsAdminOrCoach(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='ADMIN').exists() or request.user.groups.filter(name='COACH').exists()


class IsCoach(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='COACH').exists()


class IsPlayer(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='PLAYER').exists()
