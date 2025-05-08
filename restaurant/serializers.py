from rest_framework import serializers
from .models import MenuItem
# 輸入帳密後輸入錯誤會跳出alert("密碼輸入錯誤")
# from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.exceptions import AuthenticationFailed
from django.utils.translation import gettext_lazy as _

# Create your serializers here.
class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'

# 輸入帳密後輸入錯誤會跳出alert("密碼輸入錯誤") # 自訂登入錯誤訊息
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        try:
            return super().validate(attrs)
        except AuthenticationFailed:
            raise AuthenticationFailed(_("密碼錯誤，或帳號不存在，請重新確認"))
