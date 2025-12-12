from django.urls import path
from .views import (
    TarefaListCreateAPIView, 
    TarefaRetrieveUpdateDestroyAPIView, 
    LogoutView
)

urlpatterns = [
    path('tarefas/', TarefaListCreateAPIView.as_view(), name='tarefa-list-create'),
    path('tarefas/<int:pk>/', TarefaRetrieveUpdateDestroyAPIView.as_view(), name='tarefa-detail'),
    path('logout/', LogoutView.as_view(), name='logout'),
]