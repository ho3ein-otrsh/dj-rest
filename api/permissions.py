from django.http import Http404
from rest_framework.permissions import BasePermission
from rest_framework import exceptions

SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')


class IsStaffOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        return bool(
            request.user and 
            request.user.is_staff 
        )

class IsAuthorOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True
       
        return bool(
            request.user and 
            request.user.is_superuser or 

            request.user and
            request.user.is_staff and
            obj.author == request.user)

class IsStaffReadOnlyOrSuperUser(BasePermission):
    def has_permission(self, request, view):
        if bool(request.method in SAFE_METHODS and request.user and request.user.is_staff):
            return True
        return bool(request.user and request.user.is_superuser)
