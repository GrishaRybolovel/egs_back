from rest_framework.permissions import BasePermission


class DepartmentsAccessPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return self.has_read_permission(request, view)

        elif request.method == 'POST':
            return self.has_create_permission(request, view)

        elif request.method == 'PUT' or request.method == 'PATCH':
            return self.has_update_permission(request, view)

        elif request.method == 'DELETE':
            return self.has_delete_permission(request, view)

        return False

    def has_read_permission(self, request, view):

        return True

    def has_create_permission(self, request, view):
        user = request.user
        return True

    def has_update_permission(self, request, view):
        user = request.user
        return True

    def has_delete_permission(self, request, view):
        user = request.user
        return True
