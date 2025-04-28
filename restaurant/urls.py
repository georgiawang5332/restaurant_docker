from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# restaurant/urls.py
router = DefaultRouter()
router.register(r'menu-items', views.MenuItemViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_page, name='login'),  # ⬅️ 這行是新的！

    path('api/', include(router.urls)),# 你的 API
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
