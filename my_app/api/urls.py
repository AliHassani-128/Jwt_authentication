from re import L
from django.urls import path
from .views import TestAuthView, Register, LogOut
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

urlpatterns = [
    path('test/',TestAuthView.as_view(),name='auth-token'),
    path('register/', Register.as_view(), name='register'),
    path('logout/', LogOut.as_view(), name='logout'),
    path('login/', TokenObtainPairView.as_view(), name='login')
]
