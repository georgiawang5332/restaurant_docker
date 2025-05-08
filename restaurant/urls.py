from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import CustomTokenObtainPairView  # ✅ 引入自訂 View


# restaurant/urls.py
router = DefaultRouter()
router.register(r'menu-items', views.MenuItemViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_page, name='login'), 

    path('api/', include(router.urls)),# 你的 API
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), #api/token/  ← 預設 SimpleJWT 登入路由
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),  # ✅ 使用自訂 View
    
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
  