from django.urls import path
from .views import (
    TarefaListCreateAPIView,            
    TarefaRetrieveUpdateDestroyAPIView, 
    RegisterView,
    LogoutView
    # Removido: MinhaView
)

app_name = 'core'

urlpatterns = [
    # Rota para Listar (GET) e Criar (POST)
    path('tarefas/', TarefaListCreateAPIView.as_view(), name='tarefas-list'),

    # Rota para Detalhar (GET), Atualizar (PUT/PATCH) e Deletar (DELETE)
    path('tarefas/<int:pk>/', TarefaRetrieveUpdateDestroyAPIView.as_view(), name='tarefas-detail'),

    # Rotas de Autenticação
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
    # Removido: path('minha-view/', ...)
]