from .models import *
from rest_framework import serializers


class UserRoleserializer(serializers.ModelSerializer):
    class Meta:
        model = UserRole
        fields = ('ur_role', 'created_at')


class UserDetailsserializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = ('ur_id', 'user_name', 'first_name', 'last_name', 'mobile_no', 'email', 'dob', 'password', 'created_at')
