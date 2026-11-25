from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

from .models import Task
from .serializers import RegisterSerializer, TaskSerializer


# USER REGISTRATION

class RegisterView(generics.CreateAPIView):

    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save()

        token, created = Token.objects.get_or_create(user=user)

        return Response({
            "message": "User registered successfully",
            "username": user.username,
            "token": token.key
        }, status=status.HTTP_201_CREATED)


# USER LOGIN

class LoginView(ObtainAuthToken):

    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):

        response = super().post(request, *args, **kwargs)

        return Response({
            "message": "Login successful",
            "token": response.data['token']
        })


# CREATE AND VIEW TASKS

class TaskListCreateView(generics.ListCreateAPIView):

    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# UPDATE AND DELETE TASKS

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)