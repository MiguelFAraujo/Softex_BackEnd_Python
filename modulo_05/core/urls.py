from django.urls import path
from .views import (
    ListaTarefasAPIView,
    DetalheTarefaAPIView,
    MinhaView,
    LogoutView,
)

urlpatterns = [
    path('tarefas/', ListaTarefasAPIView.as_view()),
    path('tarefas/<int:pk>/', DetalheTarefaAPIView.as_view()),
    path('minha/', MinhaView.as_view()),
    path('logout/', LogoutView.as_view()),
]
