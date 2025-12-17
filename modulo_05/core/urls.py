from django.urls import path
from .views import (
    ListaTarefasAPIView,
    DetalheTarefaAPIView,
    RegisterView,
    MinhaView,
    LogoutView
)

app_name = 'core'

urlpatterns = [
    path('tarefas/', ListaTarefasAPIView.as_view(), name='tarefas-list'),
    path('tarefas/<int:pk>/', DetalheTarefaAPIView.as_view(), name='tarefas-detail'),
    path('register/', RegisterView.as_view(), name='register'),
    path('minha-view/', MinhaView.as_view(), name='minha-view'),
    path('logout/', LogoutView.as_view(), name='logout'),
]