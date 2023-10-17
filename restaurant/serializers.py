from rest_framework import serializers
from django.contrib.auth.models import User

from .models import MenuItem

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'title', 'price', 'inventory']
        model = MenuItem
