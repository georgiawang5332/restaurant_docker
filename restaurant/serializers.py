from rest_framework import serializers
from .models import MenuItem

# Create your serializers here.
class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'
