from django.db import models


# Create your models here.

class UserRole(models.Model):
    ur_id = models.AutoField(primary_key=True)
    ur_role = models.CharField(max_length=20)
    created_at = models.DateTimeField(default=True)

    def __str__(self):
        return self.ur_role


class UserDetails(models.Model):
    ud_id = models.AutoField(primary_key=True)
    ur_id = models.ForeignKey(UserRole, on_delete=models.CASCADE, null=True)
    user_name = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100,null=True)
    last_name = models.CharField(max_length=100)
    mobile_no = models.IntegerField(default=0)
    email = models.EmailField(unique=True)
    dob = models.DateField(default=0)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_name
