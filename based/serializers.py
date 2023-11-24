from .models import *
from rest_framework import serializers


class UserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRole
        fields = ('ur_role', 'created_at')


class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = ('ur_id', 'user_name', 'first_name', 'last_name', 'mobile_no', 'email', 'dob', 'password', 'created_at')
