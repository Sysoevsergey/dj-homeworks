from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
	def has_object_permission(self, request, view, obj):
		return obj.creator == request.user


class IsStaff(permissions.BasePermission):
	def has_permission(self, request, view):
		return bool(request.user and request.user.is_staff)

