from django.urls import path

from .views import (
    RegisterView,
    LoginView,
    TaskListCreateView,
    TaskDetailView
)

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('tasks/', TaskListCreateView.as_view()),
    path('tasks/<int:pk>/', TaskDetailView.as_view()),
]