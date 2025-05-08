# restaurant/permissions.py
from rest_framework.permissions import BasePermission, SAFE_METHODS

# Create your views here.

# 🔐 自訂權限：管理員才能寫，一般使用者只能看
class IsAdminOrReadOnly(BasePermission):
    """
    - GET/HEAD/OPTIONS 開放給所有登入者
    - POST/PUT/DELETE 僅限 admin（is_staff）
    or
    - 任何人都可以讀（GET、HEAD、OPTIONS）
    - 只有管理員能改（POST、PUT、DELETE）

    or
    允許所有已登入使用者讀取資料（GET、HEAD、OPTIONS），
    但只有管理員（is_staff）能進行修改（POST、PUT、DELETE）。
    """
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS: # GET, HEAD, OPTIONS
            return True #request.user and request.user.is_authenticated 
        return request.user and request.user.is_staff
