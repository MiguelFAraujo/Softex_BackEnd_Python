from django.urls import path
# Importe apenas o que existe no seu views.py
from .views import ListaTarefasAPIView, DetalheTarefaAPIView, LogoutView

urlpatterns = [
    path('tarefas/', ListaTarefasAPIView.as_view(), name='lista-tarefas'),
    path('tarefas/<int:pk>/', DetalheTarefaAPIView.as_view(), name='detalhe-tarefa'),
    path('logout/', LogoutView.as_view(), name='auth_logout'),
]