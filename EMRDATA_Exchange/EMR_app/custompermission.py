from rest_framework.permissions import BasePermission,SAFE_METHODS

class Mypermission(BasePermission):
    
    def has_permission(self, request, view):
        if request.user.groups.filter(name="Nurse's").exists():
            return True

class Procedurepermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name="Doctor's").exists():
            return True