from django.shortcuts import render
from rest_framework import generics, permissions
from .models import User
from .serializers import UserRegisterSerializer
from  rest_framework_simplejwt.views import TokenObtainPairView

# User registration
class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.AllowAny]  # anyone can register

# List all users but must be admin
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.IsAdminUser]  # only admin can see users

# Get or update current logged-in user
class UserDetailUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user