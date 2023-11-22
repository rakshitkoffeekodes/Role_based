from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_role),
    path('delete_role/<int:pk>', views.delete_role),
    path('update_role/<int:pk>', views.update_role),
    path('all_role/', views.all_role),
    path('register/', views.register),
    path('login/',views.login),
]
