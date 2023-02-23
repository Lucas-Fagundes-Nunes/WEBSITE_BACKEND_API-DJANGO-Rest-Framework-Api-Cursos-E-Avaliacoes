from rest_framework import permissions


class EhSuperUser(permissions.BasePermission):

# Se o usuário estiver fazendo a requisição de DELETE e for um super usuário, pode deletar, se não, não pode
    def has_permission(self, request, view):
        if request.method == 'DELETE':
            if request.user.is_superuser:
                return True
            return False
        return True