from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('', views.add_role),
    path('delete_role/<int:pk>', views.delete_role),
    path('update_role/<int:pk>', views.update_role),
    path('all_role/', views.all_role),
    path('register/', views.register),
    path('login/', views.login),
    # path('token/', jwt_views.TokenObtainPairView.as_view()),
    path('refresh/', jwt_views.TokenRefreshView.as_view()),
    path('verify/', jwt_views.TokenVerifyView.as_view()),
    path('auth_login/', views.auth_login),
    path('auth_register/', views.auth_register),
]
