from django.shortcuts import render

from rest_framework import viewsets
from .models import MenuItem
from .serializers import MenuItemSerializer

# 在你的 View 中，請確保已正確設定認證和權限。例如：
from rest_framework.permissions import IsAuthenticated

def index(request):
    return render(request, 'restaurant/index.html')

class MenuItemViewSet(viewsets.ModelViewSet): #用來處理 API（JSON 回應給前端） #ModelViewSet已經使用 ModelViewSet，應該已經有 POST 的功能，不用再額外寫後端。
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated]

def login_page(request):
    return render(request, 'restaurant/login.html')
