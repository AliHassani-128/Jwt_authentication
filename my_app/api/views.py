from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status
from my_app.api.serializers import UserRegisterSerializer
from django.contrib.auth.models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth import login, logout
from django.contrib.auth.models import AnonymousUser


class TestAuthView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': str(request.user), 
            'auth': str(request.auth), 
        }
        user = User.objects.get(id=request.user.id)
        login(request, user)
        if request.user.is_authenticated:
            print(user.username)
        return Response(content)


class LogOut(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if isinstance(self.request.user, AnonymousUser):
            return Response({'error':'just logged in user can log out'},status=status.HTTP_400_BAD_REQUEST)

        logout(request)
        return Response({'response':'Logged out!'})


class Register(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    model = User

    def get(self, request):
        serializer = self.get_serializer()
        return Response({'serializer': serializer})

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer.save()
            return Response({'response':'User registered'})

    def perform_create(self, serializer):

        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()
